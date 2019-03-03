from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata1 = MetaData()

view_1 = Table('views', metadata1, Column('id', Integer), Column('timestamp', Integer))
click_1 = Table('clicks', metadata1, Column('id', Integer), Column('timestamp', Integer))
click2_1 = Table('click2s', metadata1, Column('id', Integer), Column('timestamp', Integer))

metadata2 = MetaData()

view_2 = Table('views', metadata2, Column('id', Integer), Column('type', Integer), Column('timestamp', Integer))
click_2 = Table('clicks', metadata2, Column('id', Integer), Column('type', Integer), Column('timestamp', Integer))
click2_2 = Table('click2s', metadata2, Column('id', Integer), Column('type', Integer), Column('timestamp', Integer))
