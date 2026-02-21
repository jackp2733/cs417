"""
Lab 8: Build Your Own Hash Table

In this lab you will implement a hash table from scratch using
separate chaining (each bucket is a list of [key, value] pairs).

Complete the four methods marked with TODO.
Do NOT change the method signatures or the __init__ method.

Run tests:
    pytest -v
"""


class HashTable:
    """A hash table using separate chaining for collision resolution."""

    def __init__(self, size=10):
        """Create an empty hash table with the given number of buckets."""
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    # ── TODO 1: Hash Function ─────────────────────────────────────

    def _hash(self, key):
        return hash(key) % self.size

    # ── TODO 2: Put ───────────────────────────────────────────────

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.count += 1

    # ── TODO 3: Get ───────────────────────────────────────────────

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    # ── TODO 4: Delete ────────────────────────────────────────────

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return

        raise KeyError(key)

    # ── Provided Methods (do not modify) ──────────────────────────

    def __len__(self):
        """Return the number of key-value pairs in the table."""
        return self.count

    def __contains__(self, key):
        """Support 'in' operator: key in table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def load_factor(self):
        """Return the current load factor (items / buckets)."""
        return self.count / self.size

    def __repr__(self):
        """Show a readable view of the hash table's internal structure."""
        lines = []
        for i, bucket in enumerate(self.table):
            if bucket:
                pairs = ", ".join(f"{k!r}: {v!r}" for k, v in bucket)
                lines.append(f"  [{i}] {pairs}")
            else:
                lines.append(f"  [{i}] empty")
        return f"HashTable({self.count} items, {self.size} buckets):\n" + "\n".join(lines)
