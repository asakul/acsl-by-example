

#ifndef NUMERICINVERSE_SPEC_INCLUDED
#define NUMERICINVERSE_SPEC_INCLUDED

#include "AdjacentDifference.spec"
#include "PartialSum.spec"

/*@
  axiomatic NumericInverse
  {
    lemma PartialSumInverse:
      \forall value_type *a, *b, integer n;
        0 <= n               ==>
        PartialSum(a, n, b)  ==>
        AdjacentDifference(b, n, a);

    lemma AdjacentDifferenceInverse:
      \forall value_type *a, *b, integer n;
        0 <= n                       ==>
        AdjacentDifference(a, n, b)  ==>
        PartialSum(b, n, a);
  }
*/

#endif /* NUMERICINVERSE_SPEC_INCLUDED */

