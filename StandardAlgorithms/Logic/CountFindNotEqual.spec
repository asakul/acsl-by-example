
#ifndef COUNTFINDNOTEQUAL_SPEC_INCLUDED
#define COUNTFINDNOTEQUAL_SPEC_INCLUDED

#include "CountNotEqual.spec"
#include "Count.spec"

/*@
  axiomatic CountFindNotEqual
  {
    lemma CountNotEqual_AllEqual:
      \forall value_type *a, v, integer m, n;
        0 <= m <= n            ==>
        AllEqual(a, m, n, v)   ==>
        CountNotEqual(a, m, n, v) == 0;

    lemma CountNotEqual_SomeNotEqual:
      \forall value_type *a, v, integer m, n;
        0 <= m < n                     ==>
        0 < CountNotEqual(a, m, n, v)  ==>
        SomeNotEqual(a, m, n, v);

    lemma CountNotEqual_FindNotEqual:
      \forall value_type *a, v, integer m, n;
        0 <= m < n                     ==>
        0 < CountNotEqual(a, m, n, v)  ==>
        FindNotEqual(a, m, n, v) < n-m;

    lemma CountNotEqual_Zero:
      \forall value_type *a, v, integer m, n;
        0 <= m < n   ==>
        CountNotEqual(a, m, m + FindNotEqual(a, m, n, v), v) == 0;

    lemma CountNotEqual_Decrement:
      \forall value_type *a, v, integer m, n;
        0 <= m < n  ==>
        CountNotEqual(a, m + FindNotEqual(a, m, n, v), n, v) ==
        CountNotEqual(a, 0, n, v) - CountNotEqual(a, 0, m, v);
  }
*/

#endif /* COUNTFINDNOTEQUAL_H_INCLUDED */

