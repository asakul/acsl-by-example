
#ifndef BUBBLESORT_H_INCLUDED
#define BUBBLESORT_H_INCLUDED

#include "typedefs.h"
#include "Increasing.acsl"
#include "MultisetReorder.acsl"

/*@
  requires valid:       \valid(a + (0..n-1));
  assigns               a[0..n-1];
  ensures increasing:   Increasing(a, n);
  ensures reorder:      MultisetReorder{Old,Here}(a, n);
 */
void
bubble_sort(value_type* a, size_type n);

#endif /* BUBBLESORT_H_INCLUDED */
