# dvol

Docker Volume mapping control; container access made easy!

# Installation

```
brew install flare576/scripts/dvol
```

# Usage

Assuming

- `my_project` is a project using `docker compose`
- `srvc` is a service in the `docker-compose.yml`
- `my_project_srvc_1` was started with `docker compose`
- `my_project_srvc_1` has a folder `/important/folder`

```
dvol -c my_project_srvc_1 add /important/folder`
```
Will:
- Copy the folder from `my_project_srvc_1` to _/tmp/my_project_srvc_1_volumes/important/folder_
- Start a new git repository in /tmp/my_project_srvc_1_volumes/important/folder
- Create a new compose file: `~/.config/dvol/my_project`
  - Add a new section for `srvc`
  - Defining a volume `/tmp/my_project_srvc_1_volumes/important/folder:/important/folder`
- Restart the containers, adding `~/.config/dvol/my_project` as a config file

Now, _/tmp/my_project_srvc_1_volumes/important/folder_ is mapped to the container; any changes you
make (or the service makes) to the contents will be visible to both sides.

If you know you're going to be working with a given container a lot, you can setup a config:

``` sh
# Save as default
dvol -c my_project_srvc_1 --no-git --root ~/my/maps config

# adds another mapping, this time to the `root` defined in the config
dvol add /another/folder

# get rid of that old one, and its little files, too
# (omitting the -f will leave the files in-place)
dvol remove -f /important/folder

# Or as a saved profile
dvol -p mine -c mine_srvc_1 config
dvol -p mine add /src/dist
```

If you need to manually restart the cluster, the new docker-compose.yml file created by `add` will
not be included; you can re-enable it with

```
dvol enable
```

# Dev note: Deployment
```
# Bump dvol/VERSION.py Version
rm -rf dist
pip3 uninstall -y dvol
python3 -m build
pip3 install dist/dvol-*.tar.gz
dvol -v && python3 -m twine upload dist/*
```

