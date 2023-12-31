# Integration Hochwasserportal

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Integration to integrate with [hochwasserportal][hochwasserportal]._

**This integration will set up the following platforms.**

| Platform | Description                                 |
| -------- | ------------------------------------------- |
| `sensor` | Read water level from hochwasserportal API. |

## Installation

### HACS

The integration is available in HACS.

### Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `integration_blueprint`.
1. Download _all_ the files from the `custom_components/integration_blueprint/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Integration blueprint"

## Configuration is done in the UI

<!---->

## This integration is based on the integration_blueprint

https://github.com/ludeeus/integration_blueprint

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

---

[hochwasserportal]: https://www.hochwasserzentralen.de/
[commits-shield]: https://img.shields.io/github/commit-activity/y/embeddedfiedel/ha-lhp.svg?style=for-the-badge
[commits]: https://github.com/embeddedfiedel/ha-lhp/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/embeddedfiedel/ha-lhp.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-embeddedfiedel-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/embeddedfiedel/ha-lhp.svg?style=for-the-badge
[releases]: https://github.com/embeddedfiedel/ha-lhp/releases
