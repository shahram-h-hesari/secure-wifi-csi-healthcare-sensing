# Submodule Instructions

This document explains how to add RuView as a Git submodule in this repository. Using a Git submodule keeps RuView's code clearly separated from this repository's original work while allowing easy access to the original project for reference and study.

---

## Recommended Method

Git submodules are the **preferred** way to include RuView in this repository because:

- They keep third-party code completely separate from the original `src/`, `notebooks/`, and `app.py` code
- They point to the original RuView repository, so the original authors always receive proper attribution
- They do not copy files into this repository, avoiding license complications
- They allow the submodule to be updated to track upstream changes
- Cloners of this repository can choose whether to initialize the submodule

> **Important:** Do not manually copy RuView code into `src/`, `notebooks/`, or any other original pipeline folder.

---

## Add RuView as a Submodule

Run the following command from the root of this repository:

```bash
git submodule add https://github.com/ruvnet/RuView.git third_party/wifi_sensing/ruview/RuView
```

Then commit the submodule addition:

```bash
git commit -m "Add RuView as third-party WiFi sensing submodule"
```

This will:
1. Create the folder `third_party/wifi_sensing/ruview/RuView/` containing the RuView code
2. Add a `.gitmodules` entry pointing to `https://github.com/ruvnet/RuView.git`
3. Track the current HEAD commit of RuView as the pinned submodule version

---

## Clone This Repository With Submodules

If you clone this repository and want to include the RuView submodule:

```bash
git clone --recurse-submodules https://github.com/shahram-h-hesari/wifi-csi-fall-detection.git
```

If you have already cloned without submodules, initialize them manually:

```bash
git submodule update --init --recursive
```

---

## Update the Submodule

To update RuView to its latest upstream commit:

```bash
git submodule update --remote third_party/wifi_sensing/ruview/RuView
```

Then commit the updated submodule pointer:

```bash
git add third_party/wifi_sensing/ruview/RuView
git commit -m "Update RuView submodule to latest upstream"
```

---

## Remove the Submodule If Needed

To remove the RuView submodule from the repository:

```bash
# 1. Remove the submodule entry from .gitmodules
git config --file .gitmodules --remove-section submodule.third_party/wifi_sensing/ruview/RuView

# 2. Remove the submodule from the index
git rm --cached third_party/wifi_sensing/ruview/RuView

# 3. Remove the actual directory
rm -rf third_party/wifi_sensing/ruview/RuView

# 4. Remove the cached git config entry
git config --remove-section submodule.third_party/wifi_sensing/ruview/RuView

# 5. Delete the cached submodule data
rm -rf .git/modules/third_party/wifi_sensing/ruview/RuView

# 6. Commit the removal
git commit -m "Remove RuView submodule"
```

---

## Notes

- **Code separation:** RuView code must remain in `third_party/wifi_sensing/ruview/RuView/` only. Do not copy or import RuView code into `src/`, `notebooks/`, or `app.py`.
- **Submodule not initialized:** If the submodule has not been initialized, the `third_party/wifi_sensing/ruview/RuView/` directory will be empty. Run `git submodule update --init --recursive` to populate it.
- **License:** All code in the submodule remains under RuView's original MIT License. See `LICENSE_SUMMARY.md` for attribution details.
- **Pinned version:** Git submodules pin to a specific commit. If you need the latest RuView code, run `git submodule update --remote`.
- **No submodule yet:** As of May 2026, the submodule has not been added to this repository via the GitHub web UI. Use the command above from a local clone to add the submodule.

---

*Instructions created: May 2026. RuView repository: https://github.com/ruvnet/RuView*
