
#ifndef REMOVE_SPEC_INCLUDED
#define REMOVE_SPEC_INCLUDED

#include "RemovePartition.spec"

/*@
  axiomatic Remove
  {
    predicate
    Remove{K,L}(value_type* a, integer n, value_type* b, value_type v) =
      \forall integer k; 0 <= k < CountNotEqual{K}(a, n, v)  ==>
        \at(b[k],L) == \at(a[RemovePartition(a, n, v, k)],K);

    predicate
    Remove{K,L}(value_type* a, integer n, value_type v) =
      \forall integer k; 0 <= k < CountNotEqual{K}(a, n, v)  ==>
        \at(a[k],L) == \at(a[RemovePartition(a, n, v, k)],K);

    lemma Remove_Update{K,L}:
      \forall value_type *a, v, integer m;
        \let k = CountNotEqual{K}(a, m+1, v) - 1;
        0 <= m                                                  ==>
        Remove{K,L}(a, m, v)                                    ==>
        \at(a[m],K) != v                                        ==>
        \at(a[k],L) == \at(a[RemovePartition(a, m+1, v, k)],K)  ==>
        Remove{K,L}(a, m+1, v);
  }
*/

#endif /* REMOVE_SPEC_INCLUDED */

