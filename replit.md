# Mama Dance Metadata Sheet Converter

## Project Overview
A tool for converting source music metadata Excel files into submission-ready formats (currently: Afrosonic ingestion template). All processing happens client-side — no backend or server-side processing required.

**Intended deployment**: Desktop application (installer). Replit is the development environment. The app is built as a self-contained single HTML file with no external network dependencies so it packages cleanly as a desktop installer.

## Architecture
- **Frontend**: Single HTML file (`afrosonic_converter.html`) — all UI, CSS, and logic in one file
- **Electron main**: `main.js` — creates the BrowserWindow and loads the HTML file
- **Dev server**: `server.py` — minimal Python HTTP server for browser-based development (port 5000)
- **Language**: Vanilla JavaScript (no framework), Python 3.12 (dev server only), Node.js 20 (Electron)
- **Dependencies**: `xlsx.full.min.js` — bundled locally (no CDN); `electron` + `electron-builder` (build-time only)

## Key Design Decisions
- **No CDN dependencies**: All libraries and fonts are bundled locally. Works fully offline.
- **Single HTML file**: Trivially portable. No build step for the app logic. Easy to load in Electron with `mainWindow.loadFile(...)`.
- **Three-phase UX flow**: Landing → Format selection → Workspace
- **Client-side only**: Excel files are read/processed entirely in the browser/webview. No data leaves the user's machine.
- **Settings persistence**: Field mappings and EditType codes are saved to `localStorage` (Electron's `userData` folder on desktop). They survive app restarts and are not removed on uninstall unless the user opts in.

## User Flow
1. **Landing** — User drops one or more source `.xlsx` files (or clicks Browse)
2. **Format selection** — User picks a destination format (currently only AFROSONIC; others are placeholder)
3. **Workspace** — Side-by-side: file queue + export on the left, scrollable data preview on the right
4. **Settings (⚙)** — Field Mapping tab (all 113 destination columns, configurable) + EditType Codes tab

## Key Files
| File | Purpose |
|---|---|
| `afrosonic_converter.html` | Entire application — UI, conversion logic, all CSS |
| `xlsx.full.min.js` | Bundled xlsx library (v0.18.5), no CDN |
| `main.js` | Electron main process — creates BrowserWindow |
| `package.json` | Electron + electron-builder config, build scripts |
| `installer.nsh` | Custom NSIS script — adds uninstall preferences dialog |
| `.github/workflows/build.yml` | GitHub Actions — builds installers for all platforms |
| `server.py` | Dev HTTP server (port 5000), Replit development only |
| `compare_formats.py` | Utility for inspecting source/target field mappings |

## Running in Development (Replit)
The "Start application" workflow runs:
```
python3 server.py
```
Serves on `0.0.0.0:5000`. Open the preview pane to use the app in a browser.

## Building Installers

### Option 1 — GitHub Actions (recommended for production)
Push to a GitHub repository and the build workflow runs automatically.

**To produce installers:**
1. Push the project to GitHub
2. Go to **Actions** tab → **Build Installers** → **Run workflow** (manual trigger), OR
3. Push a version tag: `git tag v1.0.0 && git push --tags`

**This produces:**
- `windows-installer` artifact → `Mama Dance Metadata Converter Setup 1.0.0.exe` (NSIS)
- `macos-dmg` artifact → `Mama Dance Metadata Converter-1.0.0.dmg`
- `linux-appimage` artifact → `Mama Dance Metadata Converter-1.0.0.AppImage`

When triggered by a tag, artifacts are also attached to a GitHub Release automatically.

### Option 2 — Build locally on your own machine
Requires Node.js 20+ and (for Windows) running on a Windows machine, or macOS for the DMG.
```bash
npm install
npm run build:win    # Windows NSIS installer
npm run build:mac    # macOS DMG
npm run build:linux  # Linux AppImage
```

## Installer Behaviour (Windows NSIS)
- **Install**: Wizard-style installer with directory selection
- **Desktop shortcut**: Created automatically
- **Start Menu folder**: `Mama Dance → Mama Dance Metadata Converter` + uninstall entry
- **Apps & Features**: Registered in Windows Settings / Control Panel → uninstall from there
- **Uninstall**: Removes all app files. Prompts user whether to also delete saved settings (field mappings, EditType codes). Settings are kept by default.

## Adding New Destination Formats
1. Add a new format card in the `screenFormat` HTML section
2. Add the format's column list (equivalent of `AFRO_COLS`)
3. Add the default field mapping entries in `buildDefaultFieldMapping()`
4. Wire up the format selection logic in `handleFormatSelect`

## Road Map
- [ ] Windows code signing (requires EV certificate for no SmartScreen warning)
- [ ] App icon (`.ico` for Windows, `.icns` for macOS)
- [ ] Additional destination formats (as provided by the team)
- [ ] Auto-update support via `electron-updater`
