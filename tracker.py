import argparse
import datetime
import fileinput

parser = argparse.ArgumentParser(description="generates plain text report for expenses till date",
								epilog="creates file expensereport.txt in working directory")
parser.add_argument("-r", "--report", action="count", 
                    help="generates plain text report", required=False)
parser.add_argument( "--add-expense", action="store", type=int,
                    help="Adds expense to the file", required=False)
args = parser.parse_args()
print args
if args.report :
	print 'generating report, please wait...'
	expenseReport = open('expenseReport', "ab+")
	total=0
	with open('inputReport.txt') as f:
		for lines in f:
			print lines
			val = lines.split()
			expenseReport.write(lines)
			#num_val = lines.split()
			#total = int(num_val[1]) + total 
	expenseReport.write('\nTotal = '+ total)
	expenseReport.close()

if args.add_expense:
	inputreport = open('inputReport.txt', "ab+")
	inputreport.write('\n'+str(datetime.date.today())+'\t'+str(args.add_expense))
	inputreport.close()
	
