
#ifndef UNIQUEPARTITION_SPEC_INCLUDED
#define UNIQUEPARTITION_SPEC_INCLUDED

#include "UniqueSize.spec"
#include "AllSomeNot.spec"
#include "Unchanged.spec"

/*@
  axiomatic UniquePartition
  {
    logic integer
    UniquePartition(value_type* a, integer n, integer i) reads a[0..n-1];

    axiom UniquePartitionEmpty:
      \forall value_type *a, integer n, i;
        n <= 0  ==>  UniquePartition(a, n, i) == 0;

    axiom UniquePartitionLeft:
      \forall value_type *a, integer n, i;
        0 < n  ==>  i <= 0  ==>  UniquePartition(a, n, i) == 0;

    axiom UniquePartitionRight:
      \forall value_type *a, integer n, i;
        0 < n  ==>  UniqueSize(a, n) <= i  ==>  UniquePartition(a, n, i) == n;

    axiom UniquePartitionMonotone:
      \forall value_type *a, integer n, i, j;
        0 <= i < j <= UniqueSize(a, n)  ==>
        UniquePartition(a, n, i) < UniquePartition(a, n, j);

    axiom UniquePartitionSegment:
      \forall value_type *a, integer n, i, k;
        0 <= i < UniqueSize(a, n)  ==>
        AllEqual(a, UniquePartition(a, n, i), UniquePartition(a, n, i+1));

    axiom UniquePartitionMaximal:
      \forall value_type *a, integer n, i;
        0 <= i < UniqueSize(a, n) - 1  ==>
        a[UniquePartition(a, n, i)] != a[UniquePartition(a, n, i+1)];

    axiom UniquePartitionEqual:
      \forall value_type *a, integer n, m, i;
        n < m  ==>  0 <= i < UniqueSize(a, n)  ==>
        UniquePartition(a, n, i) == UniquePartition(a, m, i);

    axiom UniquePartitionRead{K,L}:
      \forall value_type *a, integer n, i;
        Unchanged{K,L}(a, n)  ==>
          UniquePartition{K}(a, n, i) == UniquePartition{L}(a, n, i);

    lemma UniquePartitionZero:
      \forall value_type *a, integer n;
        UniquePartition(a, n, 0) == 0;

    lemma UniquePartitionLowerBound:
      \forall value_type *a, integer n, i;
        0 < n  ==> 0 <= i < UniqueSize(a, n)  ==> 0 <= UniquePartition(a, n, i);

    lemma UniquePartitionUpperBound:
      \forall value_type *a, integer n, i;
        0 < n  ==> 0 <= i < UniqueSize(a, n)  ==>  UniquePartition(a, n, i) < n;

    lemma UniquePartitionDiffer:
      \forall value_type *a, integer i, k, n;
        UniquePartition(a, n, k-1) < i <= UniquePartition(a, n, k)  ==>
        a[i-1] != a[i]  ==>  i == UniquePartition(a, n, k);
  }
*/

#endif /* UNIQUEPARTITION_SPEC_INCLUDED */

