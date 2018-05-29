int auxfun( int a )
{
   if (a > 10) { __CPROVER_assert( 0, "aux rets 10" ); return 10; }
 
  __CPROVER_assert( 0, "aux rets a-5" );
   return a-5;
}

int minxyz( int x, int y, int z ) {
  int min;

  if (x <= y) { 
     if ( z <= x  ) 
         { min = z;
           x = 45;  y = 45 ; z = 45;
          __CPROVER_assert( 0, " z <= x <= y" ); } 
     else
         { min = x;
           __CPROVER_assert( 0, " x <= (z,y)" );  }
  }
   else {
     if ( z <= y  ) 
         { min = z;
           __CPROVER_assert( 0, " z <= y <= x" );  } 
     else
         { min = y;
           __CPROVER_assert( 0, " y <= (x,z)" );  }    
   }

__CPROVER_assert( 
   ( min <= x &&  min <= y && min <= z &&
     (  min == x |  min == y  | min ==  z  )),
   " function minxyz returns the min of x,y,z " );
  return min;
}

