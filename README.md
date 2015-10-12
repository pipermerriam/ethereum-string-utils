# Ethereum String Utils

String Utility library for ethereum contracts.

Usable as a library or to make direct calls against via `0xcca8353a18e7ab7b3d094ee1f9ddc91bdf2ca6a4`

Compiled on OSX using solc version `0.1.5-23865e39` with the `--optimize` flag enabled.


## API

* `function uintToBytes(uint v) constant returns (bytes32 ret)`

Converts an unsigned integer to it's string representation.


```javascript
> stringUtils.uintToBytes(1234)
"1234"
```


* `function bytesToUInt(uint v) constant returns (uint ret)`

Converts a numeric string to it's unsigned integer representation.


```javascript
> stringUtils.uintToBytes("1234")
1234
```
