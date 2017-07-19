import re
import pandas as pd
import sys


def generate_xlsx():

	file = open(sys.argv[-1])
	textbuffer = file.read()
	file.close()

	table=re.compile("((\|.*\n)(\|:.*\n)((\|.*\|\n)*))")
	row = re.compile("\|.*\|\n")

	m = re.findall(table, textbuffer)
	dfs = []

	for match in m:
		_columns = match[1].split("|")
		bufDF = pd.DataFrame(columns = _columns)

		print(match[3])
		m2 = re.findall(row,match[3])
		for match2 in m2:
			bufDF.loc[-1]= match2.split("|")
			bufDF.index = bufDF.index + 1

		bufDF = bufDF.drop('',1)
		bufDF = bufDF.drop('\n',1)

		dfs.append(bufDF)


	print(bufDF)

	writer = pd.ExcelWriter('draft.xlsx', engine='xlsxwriter', date_format='%m/%d/%Y')

	i = 0;
	for df in dfs:

		df.to_excel(writer, sheet_name="sheet %s" % (i), index=False)
		i = i + 1

	writer.save()

if __name__ == "__main__":
	generate_xlsx()