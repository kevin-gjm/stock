
for i in {1..365}
do
	year=`date -v -${i}d +%Y`
	day=`date -v -${i}d +%Y%m%d`
	week=`date -v -${i}d +%w`
	#echo $year
	echo $day
	if [ ${week} -gt 1 ]&&[ ${week} -lt 6 ] ; then
		echo $week
		wget http://www.czce.com.cn/cn/DFSStaticFiles/Future/${year}/${day}/FutureDataDailyTA.txt -O ${day}.txt
	fi
	

done
 
#wget http://www.czce.com.cn/cn/DFSStaticFiles/Future/2022/20220104/FutureDataDailyTA.txt