"""
Comprehensive test suite for inefficient_code.py module.
"""
import pytest
from typing import List
from inefficient_code import (
    slow_fibonacci,
    inefficient_string_concatenation,
    slow_search,
    nested_loops_processing,
    repeated_calculations,
    global_variable_function,
    InefficientClass,
    counter
)


class TestSlowFibonacci:
    """Tests for the slow_fibonacci function."""

    def test_fibonacci_base_case_zero(self):
        """Test Fibonacci of 0."""
        assert slow_fibonacci(0) == 0

    def test_fibonacci_base_case_one(self):
        """Test Fibonacci of 1."""
        assert slow_fibonacci(1) == 1

    def test_fibonacci_small_numbers(self):
        """Test Fibonacci for small numbers."""
        assert slow_fibonacci(2) == 1
        assert slow_fibonacci(3) == 2
        assert slow_fibonacci(4) == 3
        assert slow_fibonacci(5) == 5
        assert slow_fibonacci(6) == 8

    def test_fibonacci_larger_number(self):
        """Test Fibonacci for a larger number."""
        assert slow_fibonacci(10) == 55

    def test_fibonacci_negative_input(self):
        """Test Fibonacci with negative input raises ValueError."""
        with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
            slow_fibonacci(-1)

    def test_fibonacci_type_error(self):
        """Test Fibonacci with non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Expected integer"):
            slow_fibonacci(3.14)
        with pytest.raises(TypeError, match="Expected integer"):
            slow_fibonacci("5")


class TestInefficientStringConcatenation:
    """Tests for the inefficient_string_concatenation function."""

    def test_concatenation_zero(self):
        """Test with n=0."""
        assert inefficient_string_concatenation(0) == ""

    def test_concatenation_one(self):
        """Test with n=1."""
        assert inefficient_string_concatenation(1) == "0-"

    def test_concatenation_small(self):
        """Test with small n."""
        result = inefficient_string_concatenation(3)
        assert result == "0-1-2-"

    def test_concatenation_length(self):
        """Test that result length is correct."""
        n = 10
        result = inefficient_string_concatenation(n)
        # Count dashes to verify all items were added
        assert result.count('-') == n

    def test_concatenation_negative_input(self):
        """Test concatenation with negative input raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            inefficient_string_concatenation(-5)

    def test_concatenation_type_error(self):
        """Test concatenation with non-integer input raises TypeError."""
        with pytest.raises(TypeError, match="Expected integer"):
            inefficient_string_concatenation(3.14)


class TestSlowSearch:
    """Tests for the slow_search function."""

    def test_search_found_at_start(self):
        """Test finding item at the start of the list."""
        assert slow_search([1, 2, 3, 4, 5], 1) is True

    def test_search_found_at_end(self):
        """Test finding item at the end of the list."""
        assert slow_search([1, 2, 3, 4, 5], 5) is True

    def test_search_found_in_middle(self):
        """Test finding item in the middle of the list."""
        assert slow_search([1, 2, 3, 4, 5], 3) is True

    def test_search_not_found(self):
        """Test when item is not in the list."""
        assert slow_search([1, 2, 3, 4, 5], 10) is False

    def test_search_empty_list(self):
        """Test searching in an empty list."""
        assert slow_search([], 1) is False

    def test_search_with_strings(self):
        """Test searching with string values."""
        assert slow_search(['a', 'b', 'c'], 'b') is True
        assert slow_search(['a', 'b', 'c'], 'z') is False

    def test_search_type_error(self):
        """Test search with non-list input raises TypeError."""
        with pytest.raises(TypeError, match="items must be a list"):
            slow_search("not a list", 'x')
        with pytest.raises(TypeError, match="items must be a list"):
            slow_search((1, 2, 3), 2)


class TestNestedLoopsProcessing:
    """Tests for the nested_loops_processing function."""

    def test_processing_empty_list(self):
        """Test with empty list."""
        assert nested_loops_processing([]) == []

    def test_processing_all_even(self):
        """Test with all even numbers."""
        result = nested_loops_processing([2, 4, 6])
        assert result == [4, 16, 36]

    def test_processing_all_odd(self):
        """Test with all odd numbers."""
        result = nested_loops_processing([1, 3, 5])
        assert result == []

    def test_processing_mixed(self):
        """Test with mixed even and odd numbers."""
        result = nested_loops_processing([1, 2, 3, 4, 5, 6])
        assert result == [4, 16, 36]

    def test_processing_preserves_order(self):
        """Test that order is preserved."""
        result = nested_loops_processing([10, 8, 6, 4, 2])
        assert result == [100, 64, 36, 16, 4]

    def test_processing_type_error_not_list(self):
        """Test nested loops with non-list input raises TypeError."""
        with pytest.raises(TypeError, match="data must be a list"):
            nested_loops_processing("not a list")

    def test_processing_type_error_non_integers(self):
        """Test nested loops with non-integer items raises TypeError."""
        with pytest.raises(TypeError, match="All items in data must be integers"):
            nested_loops_processing([1, 2, "three", 4])


class TestRepeatedCalculations:
    """Tests for the repeated_calculations function."""

    def test_calculations_empty_list(self):
        """Test with empty list."""
        assert repeated_calculations([]) == {}

    def test_calculations_below_threshold(self):
        """Test with data length below threshold."""
        result = repeated_calculations([1, 2, 3], threshold=10)
        assert result == {}

    def test_calculations_above_threshold(self):
        """Test with data above threshold."""
        data = list(range(20))  # 0-19, length > 10
        result = repeated_calculations(data, threshold=10)
        # Should include values > 10: 11, 12, 13, ..., 19
        assert len(result) > 0
        assert all(key > 10 for key in result.keys())

    def test_calculations_values(self):
        """Test that calculations produce correct ratios."""
        data = [15, 20, 25]  # avg = 20
        result = repeated_calculations(data, threshold=2)
        assert 15 in result
        assert 20 in result
        assert 25 in result
        # Each value / avg
        assert result[20] == pytest.approx(1.0)

    def test_calculations_type_error_not_list(self):
        """Test repeated_calculations with non-list input raises TypeError."""
        with pytest.raises(TypeError, match="data must be a list"):
            repeated_calculations("not a list")

    def test_calculations_type_error_non_numeric(self):
        """Test repeated_calculations with non-numeric items raises TypeError."""
        with pytest.raises(TypeError, match="All items in data must be numeric"):
            repeated_calculations([1, 2, "three"])

    def test_calculations_negative_threshold(self):
        """Test repeated_calculations with negative threshold raises ValueError."""
        with pytest.raises(ValueError, match="threshold must be non-negative"):
            repeated_calculations([1, 2, 3], threshold=-5)


class TestGlobalVariableFunction:
    """Tests for the global_variable_function."""

    def test_global_counter_increments(self, capsys):
        """Test that global counter increments."""
        import inefficient_code
        initial = inefficient_code.counter
        global_variable_function()
        captured = capsys.readouterr()
        assert f"Counter is now {initial + 1}" in captured.out


class TestInefficientClass:
    """Tests for the InefficientClass."""

    def test_initialization_with_name_only(self):
        """Test initializing with just a name."""
        obj = InefficientClass("test")
        assert obj.name == "test"
        assert obj.values == []
        assert obj.processed == {}

    def test_initialization_with_values(self):
        """Test initializing with name and values."""
        obj = InefficientClass("test", [1, 2, 3])
        assert obj.name == "test"
        assert obj.values == [1, 2, 3]

    def test_process_values_doubles(self):
        """Test that process_values doubles each value."""
        obj = InefficientClass("test", [1, 2, 3])
        result = obj.process_values()
        assert result == {1: 2, 2: 4, 3: 6}

    def test_process_values_empty(self):
        """Test process_values with empty list."""
        obj = InefficientClass("test", [])
        result = obj.process_values()
        assert result == {}

    def test_get_stats_empty(self):
        """Test get_stats with empty values."""
        obj = InefficientClass("test", [])
        stats = obj.get_stats()
        assert stats == {"count": 0, "average": 0}

    def test_get_stats_with_values(self):
        """Test get_stats with values."""
        obj = InefficientClass("test", [1, 2, 3, 4, 5])
        stats = obj.get_stats()
        assert stats["count"] == 5
        assert stats["sum"] == 15
        assert stats["average"] == 3.0
        assert stats["max"] == 5
        assert stats["min"] == 1

    def test_get_stats_single_value(self):
        """Test get_stats with single value."""
        obj = InefficientClass("test", [42])
        stats = obj.get_stats()
        assert stats["count"] == 1
        assert stats["sum"] == 42
        assert stats["average"] == 42.0
        assert stats["max"] == 42
        assert stats["min"] == 42

    def test_class_init_type_error_name(self):
        """Test InefficientClass with non-string name raises TypeError."""
        with pytest.raises(TypeError, match="name must be a string"):
            InefficientClass(123)

    def test_class_init_type_error_values(self):
        """Test InefficientClass with non-list values raises TypeError."""
        with pytest.raises(TypeError, match="values must be a list or None"):
            InefficientClass("test", "not a list")


class TestEdgeCases:
    """Additional edge case tests."""

    def test_fibonacci_sequence_correctness(self):
        """Verify Fibonacci sequence is correct."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, exp in enumerate(expected):
            assert slow_fibonacci(i) == exp

    def test_search_with_duplicates(self):
        """Test search with duplicate values."""
        assert slow_search([1, 2, 2, 3], 2) is True

    def test_nested_loops_with_zero(self):
        """Test nested loops processing with zero."""
        result = nested_loops_processing([0, 1, 2])
        assert 0 in result  # 0 is even, 0*0 = 0

    def test_inefficient_class_reprocessing(self):
        """Test that reprocessing updates the processed dict."""
        obj = InefficientClass("test", [1, 2])
        obj.process_values()
        assert obj.processed == {1: 2, 2: 4}

        # Add more values and reprocess
        obj.values = [3, 4]
        obj.process_values()
        # Note: This overwrites, doesn't append
        assert obj.processed == {3: 6, 4: 8}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
