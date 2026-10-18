#!/usr/bin/env bash
set -ETeou pipefail

main() {
    local output="eDP-1"
    local -A transform_dict=(
        ["normal"]="normal"
        ["left-up"]="90"
        ["right-up"]="270"
        ["bottom-up"]="180"
    )

    while IFS= read -r line; do
        [[ "${line}" =~ "Accelerometer" ]] || continue
        niri \
            msg \
            output "${output}" \
            transform "${transform_dict["${line##* }"]}"
    done < <(monitor-sensor --accel)
}

main "$@"
