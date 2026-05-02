import pandas as pd
import matplotlib.pyplot as plt

# read data file with pandas

data_file = pd.read_csv("/data/intercepted_data.csv")

column_z = data_file["z"]


print("shape:", data_file.shape)
print(column_z.describe())
print("Duplicates:", column_z.duplicated().sum())


plt.hist(column_z, bins=80)
plt.title("Distribution of column z")
plt.show()

plt.plot(column_z.values)
plt.title("Sequence plot")
plt.show()


