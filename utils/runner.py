import filecmp
import glob
import os
import time
from typing import Callable, List


def run(solve: Callable[[List[str]], List[str]]):
    total_start_time = time.time()
    for input_file_path in sorted(glob.glob("*.in"), key=str.lower):
        base_name = os.path.splitext(input_file_path)[0]
        output_file_path = f"{base_name}.out"
        expect_file_path = f"{base_name}.expect"

        print(f"--- Processing: '{input_file_path}' ---")

        try:
            file_start_time = time.time()
            with open(input_file_path, "r") as f:
                input_data = f.read()

            output_data = solve(input_data.split("\n"))

            if output_data is None:
                print(
                    f"WARNING: solve() returned None for '{input_file_path}'. Skipping file."
                )
                continue

            with open(output_file_path, "w") as f:
                f.write("\n".join(output_data))
            file_duration = time.time() - file_start_time
            print(
                f"Wrote solution to: '{output_file_path}' (took {file_duration:.4f}s)"
            )

            if os.path.exists(expect_file_path):
                if filecmp.cmp(output_file_path, expect_file_path, shallow=False):
                    print(f"SUCCESS: Output matches '{expect_file_path}'.")
                else:
                    print(f"FAILURE: Output does not match '{expect_file_path}'.")

        except Exception as e:
            print(f"ERROR: An error occurred while processing '{input_file_path}': {e}")

    total_duration = time.time() - total_start_time
    print(f"--- All files processed in {total_duration:.4f}s. ---")
