# tailwindplus-downloader-folder-structure

Just a simple python script creating a folder structure using the json file produced by https://github.com/richardkmichael/tailwindplus-downloader:
```json
{
  "version": "2025-08-20-203209",
  "downloaded_at": "2025-08-20T20:32:09.813Z",
  "component_count": 657,
  "download_duration": "589.6s",
  "downloader_version": "2.0.0",
  "tailwindplus": {
    "Application UI": {
      "Application Shells": {
        "Multi-Column Layouts": {
          "Constrained three column": {
            "name": "Constrained three column",
            "snippets": [
              {
                "code": "<div...",
                "name": "html",
                "mode": "light",
                "version": 4
              },
              {
                "code": "<div....",
                "name": "react",
                "mode": "light",
                "version": 4
              },
              {
                "code": "<div....",
                "name": "vue",
                "mode": "light",
                "version": 4
              }
            ]
          }
        }
      }
    }
  }
}
```
to
```
├── tailwindplus
│   ├── Application UI
│   │   ├── Application Shells
│   │   │   ├── Multi-Column Layouts
│   │   │   │   ├── Constrained three column
│   │   │   │   │   └── v4
│   │   │   │   │       ├── Constrained three column.light.html
│   │   │   │   │       ├── Constrained three column.light.react
│   │   │   │   │       └── Constrained three column.light.vue
```

## Usage
```bash
$ python structure.py <json_file_path>
```
