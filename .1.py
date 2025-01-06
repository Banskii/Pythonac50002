import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Reading in csv file
    df = pd.read_csv("GrowLocations.csv")

    # Latitude and Longitude boundary points
    min_Lat = 50.681
    max_Lat = 57.985
    min_Long = -10.592
    max_Long = 1.6848

    # Switch column name back to correct one and filter them to be among the boundary points
    df = df.rename(columns={'Longitude': 'Latitude', 'Latitude': 'Longitude'})
    filterDf = df[(df.Longitude >= min_Long) & (df.Longitude <= max_Long) & (df.Latitude >= min_Lat) & (df.Latitude <= max_Lat)]

    # Read the map into a variable
    map_img = plt.imread("map7.png")

    # Plot the points of the df on the axes from plt.subplots
    fig, ax = plt.subplots()
    plt.title("Grow Data Plot of UK")
    ax.scatter(filterDf['Longitude'], filterDf['Latitude'], marker='x', color='red', label='Location of sensor')
    ax.imshow(map_img, extent = [min_Long, max_Long, min_Lat, max_Lat], aspect='auto')

    # plot labels and legend added from scatter label value, plots saved and shown
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.savefig('Result.png')
    plt.show()


if __name__ == '__main__':
    main()


