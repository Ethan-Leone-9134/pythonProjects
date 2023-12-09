/// Calculate the raw NEC data based on address and command.
/// Status: STABLE / Expected to work.
/// @param[in] address An address value.
/// @param[in] command An 8-bit command value.
/// @return A raw 32-bit NEC message suitable for use with `sendNEC()`.
/// @see http://www.sbprojects.net/knowledge/ir/nec.php
uint32_t IRsend::encodeNEC(uint16_t address, uint16_t command) {
  command &= 0xFF;  // We only want the least significant byte of command.
  // sendNEC() sends MSB first, but protocol says this is LSB first.
  command = reverseBits(command, 8);
  command = (command << 8) + (command ^ 0xFF);  // Calculate the new command.
  if (address > 0xFF) {                         // Is it Extended NEC?
    address = reverseBits(address, 16);
    return ((address << 16) + command);  // Extended.
  } else {
    address = reverseBits(address, 8);
    return (address << 24) + ((address ^ 0xFF) << 16) + command;  // Normal.
  }
}