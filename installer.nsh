; Custom NSIS installer/uninstaller hooks
; Included by electron-builder during Windows build

; ── After uninstall: offer to remove saved user settings ──
!macro customUninstall
  MessageBox MB_YESNO|MB_ICONQUESTION \
    "Do you also want to remove your saved settings?$\n$\n\
This includes custom field mappings and EditType configurations.$\n$\n\
Select 'No' to keep your settings in case you reinstall." \
    IDNO KeepData

  ; Remove Electron user data directory (stores localStorage / preferences)
  RMDir /r "$APPDATA\Mama Dance Metadata Converter"

  KeepData:
!macroend
