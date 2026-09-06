# Cockapoo Club · Training Bookings

A Django portfolio application for a fictional Cockapoo club, combining dog-care content with training-session bookings.

**Python · Django**

[Getting started](#getting-started) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- Member registration and account templates.
- Create and manage training-session bookings.
- Dog-care articles, gallery pages and a Django administration interface.

## Using the project

1. Start the configured Django application.
2. Register or sign in to explore the member experience.
3. Create a training-session booking and review its management controls.

> **Project notes:** The committed dependency and runtime pins come from an older project environment. Check package compatibility before deployment; configuration of the database and media service is required.

## Getting started

Requires Git, Python, pip and a virtual environment. The repository records `python-3.11.8` in [runtime.txt](runtime.txt). Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/Cockapoo-Club-PortProj4.git
cd Cockapoo-Club-PortProj4
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

After resolving the project notes and configuring the local environment, use:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Configuration

Settings are defined in [CockapooClub/settings.py](CockapooClub/settings.py). Set the values used by your chosen local configuration before running Django. A `.env` file is only read when the project explicitly loads it; most of these projects read the process environment or an optional `env.py`.

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | Connection URL for your own development database. Required where settings parse it without a fallback. |
| `DEV` | Development-mode switch. Inspect whether the settings test its presence or its value. |
| `SECRET_KEY` | Django signing key. Use a locally generated value and keep it out of Git. |

Use a disposable development database for migrations and tests. Keep service credentials and local configuration out of commits.

## Repository guide

| Path | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [manage.py](manage.py) | Django management commands |
| [CockapooClub/settings.py](CockapooClub/settings.py) | Django configuration |
| [templates/](templates/) | Server-rendered page templates |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

Hosting entry points are recorded in [Procfile](Procfile). Configure the runtime, database, allowed origins and static/media handling for the chosen host. Historical deployment records may describe services that are no longer available.

## Credits and reuse

Design decisions, original feature notes, historical testing evidence and detailed acknowledgements remain available in the preserved project record:

- [README.md · original project record](https://github.com/SamOBrienOlinger/Cockapoo-Club-PortProj4/blob/0c7a97c820cfa6ec4a3f9f5f5ad6904a519a3afd/README.md)

Learning resources and starter material: [Code Institute](https://codeinstitute.net/).

No repository-level licence file is present in this snapshot. This README does not grant additional reuse permissions. Check with the relevant rights holders before reusing code, written content or assets.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). For a problem or suggested improvement, [open an issue](https://github.com/SamOBrienOlinger/Cockapoo-Club-PortProj4/issues) with the affected page or command, steps to reproduce, and expected behaviour.

[Back to top](#cockapoo-club--training-bookings)
