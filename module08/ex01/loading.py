import numpy
import pandas
import requests
from matplotlib import pyplot
from importlib import metadata


def check_dependencies(packages):
    print("Checking dependencies:")
    for name, description in packages:
        try:
            version = metadata.version(name)
            print(f"[OK] {name} ({version}) - {description}")
        except metadata.PackageNotFoundError:
            print(f"[MISSING] {name} - {description}")


def generate_data(number_of_points):
    x = numpy.random.rand(number_of_points) * 2
    y = numpy.random.rand(number_of_points) + x * 5
    return pandas.DataFrame({'Feature_X': x, 'Target_y': y})


def plot_data(df, output_file):
    pyplot.scatter(df['Feature_X'], df['Target_y'], color='black', alpha=0.5)
    pyplot.xlabel('Feature X')
    pyplot.ylabel('Target Y')
    pyplot.title('Relationship between income and spending')
    pyplot.savefig(output_file)
    pyplot.close()


def main():
    print("\nLOADING STATUS: Initializing programs...\n")

    packages = [
        ("pandas", "Data manipulation ready"),
        ("requests", "Network access ready"),
        ("matplotlib", "Visualization ready")
    ]

    check_dependencies(packages)

    try:
        requests.get("https://www.google.com")
    except requests.RequestException:
        print("Warning: Unable to reach the internet.")

    number_of_points = 1000
    data = generate_data(number_of_points)

    output_file = "matrix_analysis.png"
    display_name = "matrix\\_analysis.png"

    print("\nAnalyzing Matrix data...")
    print(f"Processing {number_of_points} data points...")
    plot_data(data, output_file)
    print("Generating visualization...")
    print("\nAnalysis complete!")
    print(f"Results saved to: {display_name}")


if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError as e:
        print(f"Module not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
