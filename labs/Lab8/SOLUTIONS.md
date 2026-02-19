# Lab 8: Solutions — Hash Table (TA Reference)

**Do not distribute to students.**

## Solution Code

### `_hash(self, key)`

```python
def _hash(self, key):
    return hash(key) % self.size
```

One line. `hash()` returns a (possibly negative) integer, `%` in Python always returns a non-negative result when the divisor is positive, so this is safe.

### `put(self, key, value)`

```python
def put(self, key, value):
    index = self._hash(key)
    bucket = self.table[index]
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            return
    bucket.append([key, value])
    self.count += 1
```

Key points:
- Must check for existing key **before** appending (otherwise duplicates accumulate)
- `pair[1] = value` mutates in place (pair is a list, not a tuple)
- `self.count` only increments on new keys, not updates

**Common student mistake:** Forgetting the `return` after updating, causing both an update AND an append.

### `get(self, key)`

```python
def get(self, key):
    index = self._hash(key)
    bucket = self.table[index]
    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    raise KeyError(key)
```

Key points:
- Same pattern as put: hash → bucket → linear search
- `KeyError` is the standard Python exception for missing keys (matches dict behavior)

### `delete(self, key)`

```python
def delete(self, key):
    index = self._hash(key)
    bucket = self.table[index]
    for i, pair in enumerate(bucket):
        if pair[0] == key:
            del bucket[i]
            self.count -= 1
            return
    raise KeyError(key)
```

Key points:
- `enumerate` is needed to get the index for deletion
- `del bucket[i]` or `bucket.pop(i)` both work
- Must decrement `self.count`

**Common student mistake:** Using `bucket.remove(pair)` without enumerate — works but is less clear. Some students try `bucket.remove(key)` which fails because bucket contains `[key, value]` pairs, not bare keys.

## Grading Rubric (suggested)

| Component | Points | Notes |
|-----------|--------|-------|
| `_hash` works correctly | 15 | Returns int in valid range |
| `put` inserts new keys | 20 | Bucket contains the pair after put |
| `put` updates existing keys | 10 | No duplicate entries |
| `get` retrieves values | 20 | Returns correct value |
| `get` raises KeyError | 5 | On missing key |
| `delete` removes pairs | 15 | Key no longer in table |
| `delete` raises KeyError | 5 | On missing key |
| All tests pass | 10 | `pytest -v` green |
| **Total** | **100** | |

## Test Highlights

- `TestPutAndGet::test_collision_handling` uses a **2-bucket table** — students can't avoid collisions, which tests that their chaining actually works
- `TestDelete::test_delete_does_not_affect_other_keys` also uses a small table — verifies delete doesn't corrupt neighboring entries in the same bucket
- `TestContainsAndLoadFactor` exercises `__contains__` and `load_factor()` which are provided but depend on correct `put`/`get` implementations

## Discussion Points (if time)

1. **What happens as load factor increases?** (More collisions → longer chains → slower lookups)
2. **Why not just use a huge table?** (Memory waste — tradeoff between speed and space)
3. **How does Python's dict solve this?** (Open addressing instead of chaining, automatic resizing at ~2/3 load factor)
4. **Why is the average case O(1)?** (If hash function distributes evenly, each bucket has ~1 item)
