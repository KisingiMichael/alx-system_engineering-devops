#!/usr/bin/env ruby
#Find the regular expression that will match the cases 'htn' and 'hbtn'
puts ARGV[0].scan(/hb?t?n/).join
