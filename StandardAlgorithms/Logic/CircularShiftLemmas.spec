
#ifndef CIRCULARSHIFTLEMMAS_SPEC_INCLUDED
#define CIRCULARSHIFTLEMMAS_SPEC_INCLUDED

#include "ArrayBounds.spec"
#include "EqualRanges.spec"
#include "MultisetUnchanged.spec"
#include "EqualRangesLemmas.spec"

/*@
   axiomatic CircularShiftLemmas
   {
     lemma CircularShift_StrictLowerBound{K,L}:
       \forall value_type* a, integer m, n;
         StrictLowerBound{K}(a, m, n, \at(a[n],K))  ==>
         EqualRanges{K,L}(a, m, n, m+1)             ==>
         EqualRanges{K,L}(a, n, n+1, m)             ==>
         StrictLowerBound{L}(a, m+1, n+1, \at(a[m],L));

     lemma CircularShift_MultisetUnchanged{K,L}:
       \forall value_type* a, integer m, n;
         0 <= m <= n                     ==>
         EqualRanges{K,L}(a, m, n, m+1)  ==>
         EqualRanges{K,L}(a, n, n+1, m)  ==>
         MultisetUnchanged{K,L}(a, m, n+1);
   }
*/

#endif /* CIRCULARSHIFTLEMMAS_SPEC_INCLUDED */

