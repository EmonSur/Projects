package org.colourTable;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for the ColourTable class.
 */
public class ColourTableTest {

    @Test
    void testConstructorValidSizes() {
        // Valid sizes
        assertDoesNotThrow(() -> new ColourTable(2));
        assertDoesNotThrow(() -> new ColourTable(1024));
    }

    @Test
    void testConstructorInvalidSizes() {
        // Invalid sizes
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(3)); // Non-power of two
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(0)); // Less than 2
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(-1)); // Negative value
    }

    @Test
    void testAddValidRGBValues() {
        ColourTable table = new ColourTable(4);

        // Valid RGB values
        assertDoesNotThrow(() -> table.add(255, 255, 255)); // Maximum RGB
        assertDoesNotThrow(() -> table.add(0, 0, 0)); // Minimum RGB
    }

    @Test
    void testAddInvalidRGBValues() {
        ColourTable table = new ColourTable(4);

        // Invalid RGB values
        assertThrows(IllegalArgumentException.class, () -> table.add(-1, 100, 100)); // Invalid red
        assertThrows(IllegalArgumentException.class, () -> table.add(256, 100, 100)); // Invalid red
        assertThrows(IllegalArgumentException.class, () -> table.add(100, -1, 100)); // Invalid green
        assertThrows(IllegalArgumentException.class, () -> table.add(100, 256, 100)); // Invalid green
        assertThrows(IllegalArgumentException.class, () -> table.add(100, 100, -1)); // Invalid blue
        assertThrows(IllegalArgumentException.class, () -> table.add(100, 100, 256)); // Invalid blue
    }

    @Test
    void testAddColorsBeforeAndBeyondCapacity() {
        ColourTable table = new ColourTable(4);
        table.add(10, 20, 30);
        table.add(40, 50, 60);
        table.add(70, 80, 90);
        table.add(100, 110, 120);

        assertEquals(4, table.getColors().size()); // Ensure capacity limit works

        // Exceeding capacity
        assertThrows(IllegalStateException.class, () -> table.add(0, 0, 255));
    }
}
