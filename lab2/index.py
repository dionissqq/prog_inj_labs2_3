import pytest

from classes import Directory, BinaryFile, LogTextFile, BufferFile, NODE_TYPES

root = Directory('root')

def test_folders():
    assert root!=None
    root.create('dir1', NODE_TYPES['dir'])
    root.create('dir2', NODE_TYPES['dir'])
    root.create('dir3', NODE_TYPES['dir'])
    assert len(root.items)==3
    assert root.create('dir2', NODE_TYPES['dir'])==-1
    assert root.create('bin_file', NODE_TYPES['bin'])==-1
    # >than max_elems
    assert root.create('bin_file1', NODE_TYPES['bin'])==-1


def test_items():
    dir1 = root.items['dir1']
    assert dir1!=None
    assert dir1.create('dir1_binfile1', NODE_TYPES['bin'])==1
    assert dir1.create('dir1_log_file1', NODE_TYPES['log'])==1
    assert dir1.create('dir1_buff_file1', NODE_TYPES['buff'])==1
    assert len(dir1.items)==3
    assert dir1.items['dir1_log_file1'].readfile() == ''
    dir1.items['dir1_log_file1'].append_str('jdsfnjdn')
    assert dir1.items['dir1_log_file1'].readfile() != ''
    assert dir1.items['dir1_buff_file1'].append('el1')
    assert dir1.items['dir1_buff_file1'].append('el2')
    assert dir1.items['dir1_buff_file1'].consume() == 'el1'
    

def test_delete_move():
    dir1 = root.items['dir1']
    assert dir1.move_item('dir1_buff_file1', root)==-1
    root.list_items()
    assert root.delete('dir2')==1
    root.list_items()
    assert dir1.move_item('dir1_buff_file1', root)==1
    root.list_items()