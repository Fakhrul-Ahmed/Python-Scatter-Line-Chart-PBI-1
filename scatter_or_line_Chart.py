    # The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

    # dataset = pandas.DataFrame(Daily Rainfall, Particulate)
    # dataset = dataset.drop_duplicates()

    # Paste or type your script code here:

import matplotlib as mb
mb.rcParams['font.size']=20
import matplotlib.pyplot as plt

    # plt.plot(dataset.DailyRainfall, dataset.Particulate)

        # 'o' for scatter chart
        # '-' for line chart
        # '--' for dashed line chart
        # 'r--' for red dashed line chart
        # 'go-' for green scattered line chart
        # 'go' for green scattered chart

    # Writing the x-axis and y-axis within the plot
    # In the name: do not use a space such as Daily Rainfall. Write the name without a space in the chart & in the script

plt.plot(dataset.DailyRainfall, dataset.Particulate, 'go-')

    # for bar chart use bar int the place of plot and remove scatter option and give width

    #plt.bar(dataset.DailyRainfall, dataset.Particulate, width=0.1)

    # naming the x-axis and y-axis
plt.xlabel('Daily Rainfall')
plt.ylabel('Particulate')

plt.show()