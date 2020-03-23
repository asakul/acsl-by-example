
#ifndef INNERPRODUCT_SPEC_INCLUDED
#define INNERPRODUCT_SPEC_INCLUDED

#include "UnchangedLemmas.spec"

/*@
  axiomatic InnerProduct
  {
    logic integer
    InnerProduct{L}(value_type* a, value_type* b, integer n,
                    value_type init) =
      n <= 0 ? init : InnerProduct(a, b, n-1, init) + (a[n-1] * b[n-1]);

    lemma InnerProductRead{K,L}:
      \forall value_type *a, *b, init, integer n;
        Unchanged{K,L}(a, n)  ==>
        Unchanged{K,L}(b, n)  ==>
        InnerProduct{K}(a, b, n, init) == InnerProduct{L}(a, b, n, init);

    predicate
    ProductBounds(value_type* a, value_type* b, integer n) =
      \forall integer i; 0 <= i < n  ==>
        VALUE_TYPE_MIN <= a[i] * b[i] <= VALUE_TYPE_MAX;

    predicate
    InnerProductBounds(value_type* a, value_type* b, integer n,
                       value_type init) =
      \forall integer i; 0 <= i <= n  ==>
        VALUE_TYPE_MIN <= InnerProduct(a, b, i, init) <= VALUE_TYPE_MAX;
  }
*/

#endif /* INNERPRODUCT_SPEC_INCLUDED */

