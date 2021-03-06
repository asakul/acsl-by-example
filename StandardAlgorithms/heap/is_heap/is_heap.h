
#ifndef IS_HEAP_H_INCLUDED
#define IS_HEAP_H_INCLUDED

#include "Heap.acsl"

/*@
   requires valid: \valid_read(a +(0..n-1));
   assigns         \nothing;
   ensures heap:   \result <==> Heap(a, n);
*/
bool
is_heap(const value_type* a, size_type n);

#endif /* IS_HEAP_H_INCLUDED */

