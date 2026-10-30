package qacrypto

import (
	"crypto/cipher"

	"github.com/aegis-aead/go-libaegis/aegis128l"
	"github.com/oasisprotocol/deoxysii"
	"golang.org/x/crypto/xtea"
)

func newLegacyBlock(key []byte) (cipher.Block, error) {
	return xtea.NewCipher(key)
}

func sealFast(key, nonce, plaintext []byte) ([]byte, error) {
	aead, err := aegis128l.New(key, 16)
	if err != nil {
		return nil, err
	}
	return aead.Seal(nil, nonce, plaintext, nil), nil
}

func sealMisuseResistant(key, nonce, plaintext []byte) []byte {
	aead, _ := deoxysii.New(key)
	return aead.Seal(nil, nonce, plaintext, nil)
}
