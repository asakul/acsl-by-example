
#ifndef ACCUMULATE_SPEC_INCLUDED
#define ACCUMULATE_SPEC_INCLUDED

#include "UnchangedLemmas.spec"
#include "limits.h"

/*@
  axiomatic Accumulate
  {
    logic integer
    Accumulate{L}(value_type* a, integer n, integer init) =
      n <= 0 ? init : Accumulate(a, n-1, init) + a[n-1];

    predicate
    AccumulateBounds{L}(value_type* a, integer n, value_type init) =
      \forall integer i; 0 <= i <= n  ==>
        VALUE_TYPE_MIN <= Accumulate(a, i, init) <= VALUE_TYPE_MAX;

    lemma AccumulateRead{K,L}:
      \forall value_type *a, integer n, init;
        Unchanged{K,L}(a, n)  ==>
        Accumulate{K}(a, n, init) == Accumulate{L}(a, n, init);
  }
*/

#endif /* ACCUMULATE_SPEC_INCLUDED */

