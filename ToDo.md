##  The Structure of the MCC

##  MCC File Operations

save( self, saveas=None, clobber=False )
open( self, file_name )

##  ASCII File Operations

write( self, cat_name, file_name )
write_fits( self, file_name, clobber=False )

##  Extensions

append( self, cat_name, catalog, Rc=1, images=None )
update( self )
find_neighbors( self )
add_catalog( self, cat_name, catalog, Rc, append=True, images=None )

##  Image Operations

get_stamp( self, id, file_names, names=None, shape )
