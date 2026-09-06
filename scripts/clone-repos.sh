#!/usr/bin/env bash
set -euo pipefail

workspace_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$workspace_dir"

clone_repo() {
  local remote="$1"
  local target="$2"
  if [[ -d "$target/.git" ]]; then
    printf '%s already present\n' "$target"
    return
  fi
  git clone "$remote" "$target"
}

clone_repo https://github.com/nazareth-depinte/municipal-official-operations.git repos/official-operations
clone_repo https://github.com/nazareth-depinte/municipal-oversight.git repos/oversight
clone_repo https://github.com/nazareth-depinte/municipal-service-platform.git repos/service-platform

