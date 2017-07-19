import pandas as pd
import sys
import progressbar



def generate_md_from_xlsx():

	file = pd.ExcelFile(sys.argv[-1])
	
	dfs = []
	for sheet in file.sheet_names:
		print(sheet)
		bufDF = pd.read_excel(sys.argv[-1], sheet)
		outputfile = open(sheet+ ".md", "w+")
		columns = bufDF.columns
		stringbuffer = '|'.join(columns)
		stringbuffer = stringbuffer + "\n"
		for c in columns:
			stringbuffer = stringbuffer + "|:--"

		stringbuffer = stringbuffer + "|\n"

		valuesList = bufDF.values.tolist()
		for values in valuesList:
			stringbuffer = stringbuffer+ ("|".join(str(v) for v in values))
			stringbuffer = stringbuffer + "\n"


		outputfile.write(stringbuffer)

		outputfile.close()



if __name__ == "__main__":
	generate_md_from_xlsx()