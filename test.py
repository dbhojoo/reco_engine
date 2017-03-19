print
print 'This is a Text Multiplier script'
print
print 'WIP - press any key to continue'
raw_input()
print

text_in = str(raw_input('What shall we input at text to multiply? >>> '))
print
times = int(raw_input('How many times to multiply? >>> '))
print

for i in range(times):
	print "%s" % text_in	
	
print