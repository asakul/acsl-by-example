
#ifndef ARRAYEXTREMA_SPEC_INCLUDED
#define ARRAYEXTREMA_SPEC_INCLUDED

#include "ArrayBounds.spec"

/*@
  axiomatic ArrayExtrema
  {
    predicate
    MaxElement{L}(value_type* a, integer n, integer max) =
      0 <= max < n && UpperBound(a, n, a[max]);

    predicate
    MinElement{L}(value_type* a, integer n, integer min) =
      0 <= min < n && LowerBound(a, n, a[min]);
  }
*/

#endif /* ARRAYEXTREMA_SPEC_INCLUDED */

