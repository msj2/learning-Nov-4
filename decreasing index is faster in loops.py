import time
limit = 1000
i = 0
for i in xrange(0, 100, 1):
	limit = limit * 10
	t1 = time.time()
	for x in xrange(1,limit):
		pass
	t2 = time.time()
	inc = t2 - t1

	t1 = time.time()
	for x in xrange(limit, 1, -1):
		pass
	t2 = time.time()
	dec = t2 - t1
	print (limit, " Increasing index = ", inc, '\nDecreasing index = ', dec)
