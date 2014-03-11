from boto.s3.connection import S3Connection
aws_access_key_id ='AKIAJOLKJXGZGDTHRFSQ'
aws_secret_access_key ='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'
conn = S3Connection(aws_access_key_id, aws_secret_access_key)

from boto.s3.connection import Location
print '\n'.join(i for i in dir(Location) if i[0].isupper())
conn.create_bucket('hung.test.silicon')
bucket=conn.create_bucket('hung.test.silicon1')

key = bucket.new_key('examples/first_file.cvs')
key.set_contents_from_filename('hung.txt')
key.set_acl('public-read')

s3= boto.connect_s3(aws_access_key_id, aws_secret_access_key)
key=s3.get_bucket('hung.test.silicon1').get_key('examples/first_file.cvs')
new_key=key.copy('hung.test.collition', 'sample/file.csv')

from boto.s3.key import Key
k=Key(bucket)
k.key ='foobar'
k.set_contents_from_string("This is test of s3")

b=s3.get_bucket('hung.test.silicon1')
k=Key(b)
k.key='foobar'
k.get_contents_as_string()

rs =s3.get_all_buckets()
len(rs)
for b in rs:
  print b.name
