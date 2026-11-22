# Part 21: recorded-video status clarity

The capabilities card now shows general person and vehicle detection as available. Face/reference matching, weapon detection and number-plate recognition remain explicitly unavailable. Removed the misleading disabled checkboxes; no additional AI model is installed.

Object observations counts actual saved detections across sampled frames, including repeat appearances, and resets when selecting/removing a video. Saved-history badges reflect whether AI completed. Opening history loads its saved video, details and counters and clears the previous upload selection, preventing accidental processing of the previous local file.

Only frontend source and this note change. Existing appearance, database, model files and API behavior are retained. TypeScript checking and Vite production build passed. Run the installer while the app is open, then refresh the page; no backend restart is needed.
