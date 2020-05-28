import openseespy.opensees as ops

pid = ops.getPID()
np = ops.getNP()

# datatype = 'float'
# datatype = 'int'
datatype = 'str'

if pid == 0:
    print('Random: ')

    for i in range(1, np):
        data = ops.recv('-pid', 'ANY')
        print(data)
else:
    if datatype == 'str':
        ops.send('-pid', 0, 'Hello from {}'.format(pid))
    elif datatype == 'float':
        ops.send('-pid', 0, float(pid))
    elif datatype == 'int':
        ops.send('-pid', 0, int(pid))

ops.barrier()

if pid == 0:
    print('\nOrdered: ')

    for i in range(1, np):
        data = ops.recv('-pid', i)
        print(data)
else:
    if datatype == 'str':
        ops.send('-pid', 0, 'Hello from {}'.format(pid))
    elif datatype == 'float':
        ops.send('-pid', 0, float(pid))
    elif datatype == 'int':
        ops.send('-pid', 0, int(pid))

ops.barrier()
if pid == 0:
    print('\nBroadcasting: ')
    if datatype == 'str':
        ops.Bcast('Hello from {}'.format(pid))
    elif datatype == 'float':
        ops.Bcast(float(pid))
    elif datatype == 'int':
        ops.Bcast(int(pid))
else:
    data = ops.Bcast()
    print(data)
