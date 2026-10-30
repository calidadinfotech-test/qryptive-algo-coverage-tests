package com.qa.crypto;

import java.security.Signature;
import javax.xml.crypto.dsig.SignatureMethod;
import javax.xml.crypto.dsig.XMLSignatureFactory;
import org.bouncycastle.crypto.agreement.ECMQVBasicAgreement;
import org.bouncycastle.crypto.params.MQVPrivateParameters;

public class PublicKeyAlgos {

    public byte[] agreeWithPartner(MQVPrivateParameters ours, org.bouncycastle.crypto.CipherParameters theirs) {
        ECMQVBasicAgreement agreement = new ECMQVBasicAgreement();
        agreement.init(ours);
        return agreement.calculateAgreement(theirs).toByteArray();
    }

    public Signature germanEcSigner() throws Exception {
        return Signature.getInstance("SHA256withECGDSA", "BC");
    }

    public Signature jcaEcdsaSigner() throws Exception {
        return Signature.getInstance("SHA256withECDSA");
    }

    public SignatureMethod xmlSignatureMethod(XMLSignatureFactory factory) throws Exception {
        return factory.newSignatureMethod("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256", null);
    }
}
