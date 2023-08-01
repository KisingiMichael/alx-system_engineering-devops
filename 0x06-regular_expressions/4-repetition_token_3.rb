#!/usr/bin/env ruby
#Find the regular expression that will match 'hbn', 'hbtn', 'hbttn', 'hbtttn' and 'hbttttn' cases
puts ARGV[0].scan(/hbt*n/).join
