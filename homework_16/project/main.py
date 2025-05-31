import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print("python main.py ")
        sys.exit(1)

    file_name = sys.argv[1]

    script_content = [1]
      print("Бул my_scripts.py файлы иштеп жатат!")
      print("Салам дүйнө!")

    with open(file_name, "w", encoding="utf-8") as script_file:
        script_file.write(script_content)

    try:
        result = subprocess.run(
            ["python", file_name], capture_output=True, text=True, check=True
        )

        with open("output.txt", "w", encoding="utf-8") as output_file:
            output_file.write(result.stdout)
        print("Натыйжа output.txt")
    except subprocess.CalledProcessError as e:
        print(f"Ката чыкты: {e}")
        with open("output.txt", "w", encoding="utf-8") as output_file:
            output_file.write(e.stderr)


if __name__ == "__main__":
    main()
