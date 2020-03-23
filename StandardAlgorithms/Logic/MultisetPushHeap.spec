
#ifndef MULTISETPUSHHEAP_SPEC_INCLUDED
#define MULTISETPUSHHEAP_SPEC_INCLUDED

#include "MultisetOperations.spec"
#include "MultisetRetain.spec"
#include "MultisetUnchanged.spec"

/*@
  axiomatic MultisetPushHeap
  {
    lemma MultisetPushHeapRetain{K,L,M}:
     \forall value_type *a, ap, ah, v, integer h, p, n;
       0 <= p < h < n-1                      ==>
       ah < ap < v                           ==>
       \at(a[h],L)  ==  ah                   ==>
       \at(a[p],L)  ==  ap                   ==>
       \at(a[h],M)  ==  ap                   ==>
       MultisetMinus{K,L}(a, n, v)           ==>
       MultisetAdd{K,L}(a, n, ah)            ==>
       MultisetRetainRest{K,L}(a, n, v, ah)  ==>
       MultisetUnchanged{L,M}(a, 0, h)       ==>
       MultisetUnchanged{L,M}(a, h+1, n)     ==>
       MultisetRetainRest{K,M}(a, n, v, ap);

   lemma MultisetPushHeapClosure{K,L,M}:
     \forall value_type *a, u, v, integer i, n;
       0 <= i < n-1                         ==>
       u != v                               ==>
       \at(a[i],M)  == v                    ==>
       MultisetAdd{K,L}(a, n, u)            ==>
       MultisetMinus{K,L}(a, n, v)          ==>
       MultisetRetainRest{K,L}(a, n, v, u)  ==>
       MultisetUnchanged{L,M}(a, 0, i)      ==>
       MultisetUnchanged{L,M}(a, i+1, n)    ==>
       MultisetAdd{L,M}(a, n, v)            ==>
       MultisetMinus{L,M}(a, n, u)          ==>
       MultisetUnchanged{K,M}(a, n);
  }
*/

#endif /* MULTISETPUSHHEAP_SPEC_INCLUDED */

