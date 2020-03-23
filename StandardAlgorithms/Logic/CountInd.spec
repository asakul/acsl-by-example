
#ifndef COUNTIND_SPEC_INCLUDED
#define COUNTIND_SPEC_INCLUDED

#include "typedefs.h"

/*@
  inductive CountInd{L}(value_type *a, integer n, value_type v, integer sum)
  {
    case Nil{L}:
      \forall value_type *a, v, integer n;
        n <= 0  ==>  CountInd{L}(a, n, v, 0);

    case Hit{L}:
      \forall value_type *a, v, integer n, sum;
        0 < n  &&  a[n-1] == v  &&  CountInd{L}(a, n-1, v, sum)  ==>
        CountInd{L}(a, n, v, sum + 1);

    case Miss{L}:
      \forall value_type *a, v, integer n, sum;
        0 < n  &&  a[n-1] != v  &&  CountInd{L}(a, n-1, v, sum)  ==>
        CountInd{L}(a, n, v, sum);
  }
*/

#endif /* COUNTIND_SPEC_INCLUDED */

