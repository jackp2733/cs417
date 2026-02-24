"""
Lab 9: Tombstone Tests — YOU WRITE THESE.

Each test function has a description of what to test.
Your job is to write the implementation. Use the tests in
test_hash_table.py as examples for how to write assertions.

Run your tests:
    pytest -v -k "TestTombstones"
"""

from hash_table_open import HashTableOpen


class TestTombstones:
    """Tests that tombstones keep the hash table working correctly."""

    def test_probe_chain_survives_deletion(self):
        ht = HashTableOpen(size=3)

    # Force collisions: 0, 3, 6 all map to 0 % 3 == 0
        ht.put(0, "a")
        ht.put(3, "b")
        ht.put(6, "c")

        ht.delete(3)  # delete middle of probe chain

        assert ht.get(6) == "c"   
        assert 6 in ht               
       
        pass  # TODO: write this test

    def test_tombstone_slot_reused_on_insert(self):
        ht = HashTableOpen(size=3)

        ht.put("x", 1)
        ht.put("y", 2)
        assert len(ht) == 2

        ht.delete("x")
        assert len(ht) == 1

        ht.put("z", 3)

        assert len(ht) == 2
        assert ht.get("z") == 3
       
        pass  # TODO: write this test

    def test_count_correct_through_delete_and_reinsert(self):
        ht = HashTableOpen(size=5)

        ht.put("a", 1)
        ht.put("b", 2)
        ht.put("c", 3)
        assert len(ht) == 3

        ht.delete("b")
        assert len(ht) == 2
        assert "b" not in ht

        ht.put("b", 999)
        assert len(ht) == 3
        assert ht.get("b") == 999
       
        pass  # TODO: write this test
