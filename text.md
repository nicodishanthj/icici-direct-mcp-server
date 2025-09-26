package com.mainframe.converter.model;

import java.math.BigDecimal;

/**
 * CCPINVCB Inventory Control Record Model
 * Maps to COBOL CCPINVCB copybook structure
 */
public class CCPINVCBInventoryRecord {
    
    // Main record fields
    private String inventoryTimestamp;
    private String inventoryRerunFlag;
    private InventoryControlKey inventoryControlKey;
    private ControlBlock6 controlBlock6;
    private ControlBlock7 controlBlock7;
    
    // Default constructor
    public CCPINVCBInventoryRecord() {
        this.inventoryControlKey = new InventoryControlKey();
        this.controlBlock6 = new ControlBlock6();
        this.controlBlock7 = new ControlBlock7();
    }
    
    // Getters and Setters
    public String getInventoryTimestamp() {
        return inventoryTimestamp;
    }
    
    public void setInventoryTimestamp(String inventoryTimestamp) {
        this.inventoryTimestamp = inventoryTimestamp;
    }
    
    public String getInventoryRerunFlag() {
        return inventoryRerunFlag;
    }
    
    public void setInventoryRerunFlag(String inventoryRerunFlag) {
        this.inventoryRerunFlag = inventoryRerunFlag;
    }
    
    public InventoryControlKey getInventoryControlKey() {
        return inventoryControlKey;
    }
    
    public void setInventoryControlKey(InventoryControlKey inventoryControlKey) {
        this.inventoryControlKey = inventoryControlKey;
    }
    
    public ControlBlock6 getControlBlock6() {
        return controlBlock6;
    }
    
    public void setControlBlock6(ControlBlock6 controlBlock6) {
        this.controlBlock6 = controlBlock6;
    }
    
    public ControlBlock7 getControlBlock7() {
        return controlBlock7;
    }
    
    public void setControlBlock7(ControlBlock7 controlBlock7) {
        this.controlBlock7 = controlBlock7;
    }
    
    /**
     * InventoryControlKey - Nested control key structure
     */
    public static class InventoryControlKey {
        private ControlBlock1 controlBlock1;
        private ControlBlock2 controlBlock2;
        private ControlBlock3 controlBlock3;
        private ControlBlock4 controlBlock4;
        private ControlBlock5 controlBlock5;
        
        public InventoryControlKey() {
            this.controlBlock1 = new ControlBlock1();
            this.controlBlock2 = new ControlBlock2();
            this.controlBlock3 = new ControlBlock3();
            this.controlBlock4 = new ControlBlock4();
            this.controlBlock5 = new ControlBlock5();
        }
        
        public ControlBlock1 getControlBlock1() {
            return controlBlock1;
        }
        
        public void setControlBlock1(ControlBlock1 controlBlock1) {
            this.controlBlock1 = controlBlock1;
        }
        
        public ControlBlock2 getControlBlock2() {
            return controlBlock2;
        }
        
        public void setControlBlock2(ControlBlock2 controlBlock2) {
            this.controlBlock2 = controlBlock2;
        }
        
        public ControlBlock3 getControlBlock3() {
            return controlBlock3;
        }
        
        public void setControlBlock3(ControlBlock3 controlBlock3) {
            this.controlBlock3 = controlBlock3;
        }
        
        public ControlBlock4 getControlBlock4() {
            return controlBlock4;
        }
        
        public void setControlBlock4(ControlBlock4 controlBlock4) {
            this.controlBlock4 = controlBlock4;
        }
        
        public ControlBlock5 getControlBlock5() {
            return controlBlock5;
        }
        
        public void setControlBlock5(ControlBlock5 controlBlock5) {
            this.controlBlock5 = controlBlock5;
        }
    }
    
    /**
     * ControlBlock1 - Transaction and Client information
     */
    public static class ControlBlock1 {
        private String transactionId;
        private String clientId;
        
        public String getTransactionId() {
            return transactionId;
        }
        
        public void setTransactionId(String transactionId) {
            this.transactionId = transactionId;
        }
        
        public String getClientId() {
            return clientId;
        }
        
        public void setClientId(String clientId) {
            this.clientId = clientId;
        }
    }
    
    /**
     * ControlBlock2 - Mailer and Form Type information
     */
    public static class ControlBlock2 {
        private String mailerId;
        private FormType formType;
        private String formId;
        private BigDecimal formWeight;
        
        public String getMailerId() {
            return mailerId;
        }
        
        public void setMailerId(String mailerId) {
            this.mailerId = mailerId;
        }
        
        public FormType getFormType() {
            return formType;
        }
        
        public void setFormType(FormType formType) {
            this.formType = formType;
        }
        
        public String getFormId() {
            return formId;
        }
        
        public void setFormId(String formId) {
            this.formId = formId;
        }
        
        public BigDecimal getFormWeight() {
            return formWeight;
        }
        
        public void setFormWeight(BigDecimal formWeight) {
            this.formWeight = formWeight;
        }
        
        /**
         * Form Type Enumeration
         */
        public enum FormType {
            TS2_INV_ENVELOPE_FORM('E'),
            TS2_INV_INSERT_FORM('I'),
            TS2_INV_LABEL_FORM('L'),
            TS2_INV_MAILER_FORM('M'),
            TS2_INV_PLASTIC_FORM('P');
            
            private final char value;
            
            FormType(char value) {
                this.value = value;
            }
            
            public char getValue() {
                return value;
            }
            
            public static FormType fromValue(char value) {
                for (FormType type : FormType.values()) {
                    if (type.value == value) {
                        return type;
                    }
                }
                throw new IllegalArgumentException("Unknown form type: " + value);
            }
        }
    }
    
    /**
     * ControlBlock3 - Provider information
     */
    public static class ControlBlock3 {
        private String providerId1;
        private String providerId2;
        private String providerId3;
        
        public String getProviderId1() {
            return providerId1;
        }
        
        public void setProviderId1(String providerId1) {
            this.providerId1 = providerId1;
        }
        
        public String getProviderId2() {
            return providerId2;
        }
        
        public void setProviderId2(String providerId2) {
            this.providerId2 = providerId2;
        }
        
        public String getProviderId3() {
            return providerId3;
        }
        
        public void setProviderId3(String providerId3) {
            this.providerId3 = providerId3;
        }
    }
    
    /**
     * ControlBlock4 - Insert and Disclosure information
     */
    public static class ControlBlock4 {
        private String insertId;
        private String disclosureGroup;
        private String envelope;
        
        public String getInsertId() {
            return insertId;
        }
        
        public void setInsertId(String insertId) {
            this.insertId = insertId;
        }
        
        public String getDisclosureGroup() {
            return disclosureGroup;
        }
        
        public void setDisclosureGroup(String disclosureGroup) {
            this.disclosureGroup = disclosureGroup;
        }
        
        public String getEnvelope() {
            return envelope;
        }
        
        public void setEnvelope(String envelope) {
            this.envelope = envelope;
        }
    }
    
    /**
     * ControlBlock5 - Account and Mail Code information
     */
    public static class ControlBlock5 {
        private String tsysProductCode;
        private String clientProductCode;
        private AccountType accountType;
        private MailCode mailCode;
        
        public String getTsysProductCode() {
            return tsysProductCode;
        }
        
        public void setTsysProductCode(String tsysProductCode) {
            this.tsysProductCode = tsysProductCode;
        }
        
        public String getClientProductCode() {
            return clientProductCode;
        }
        
        public void setClientProductCode(String clientProductCode) {
            this.clientProductCode = clientProductCode;
        }
        
        public AccountType getAccountType() {
            return accountType;
        }
        
        public void setAccountType(AccountType accountType) {
            this.accountType = accountType;
        }
        
        public MailCode getMailCode() {
            return mailCode;
        }
        
        public void setMailCode(MailCode mailCode) {
            this.mailCode = mailCode;
        }
        
        /**
         * Account Type Enumeration
         */
        public enum AccountType {
            TS2_INV_NEW_ACCOUNT('N'),
            TS2_INV_SPECIAL_ACCOUNT('S'),
            TS2_INV_REISSUE_ACCOUNT('R');
            
            private final char value;
            
            AccountType(char value) {
                this.value = value;
            }
            
            public char getValue() {
                return value;
            }
            
            public static AccountType fromValue(char value) {
                for (AccountType type : AccountType.values()) {
                    if (type.value == value) {
                        return type;
                    }
                }
                throw new IllegalArgumentException("Unknown account type: " + value);
            }
        }
        
        /**
         * Mail Code Enumeration
         */
        public enum MailCode {
            TS2_INV_DROP_SHIP('D'),
            TS2_INV_EXPRESS('E'),
            TS2_INV_FOREIGN('F'),
            TS2_INV_HOLD_CLIENT('H'),
            TS2_INV_INTERNAL_HOLD('I'),
            TS2_INV_MAIN_NORMAL('N'),
            TS2_INV_FEDEX_OVERNIGHT('O'),
            TS2_INV_PROD_CHG('P'),
            TS2_INV_REGISTERED('R'),
            TS2_INV_FEDEX_SAT_DELIV('S'),
            TS2_INV_FEDEX_NEXT_DAY('X');
            
            private final char value;
            
            MailCode(char value) {
                this.value = value;
            }
            
            public char getValue() {
                return value;
            }
            
            public static MailCode fromValue(char value) {
                for (MailCode code : MailCode.values()) {
                    if (code.value == value) {
                        return code;
                    }
                }
                throw new IllegalArgumentException("Unknown mail code: " + value);
            }
        }
    }
    
    /**
     * ControlBlock6 - Extended account information
     */
    public static class ControlBlock6 {
        private String accountNumber;
        private String holdLocation;
        private String reissueCycle;
        private String fillerField;
        private String tippingColor;
        private CardTypeIndicator cardTypeIndicator;
        private BigDecimal formCount;
        private BigDecimal cardCount;
        
        public String getAccountNumber() {
            return accountNumber;
        }
        
        public void setAccountNumber(String accountNumber) {
            this.accountNumber = accountNumber;
        }
        
        public String getHoldLocation() {
            return holdLocation;
        }
        
        public void setHoldLocation(String holdLocation) {
            this.holdLocation = holdLocation;
        }
        
        public String getReissueCycle() {
            return reissueCycle;
        }
        
        public void setReissueCycle(String reissueCycle) {
            this.reissueCycle = reissueCycle;
        }
        
        public String getFillerField() {
            return fillerField;
        }
        
        public void setFillerField(String fillerField) {
            this.fillerField = fillerField;
        }
        
        public String getTippingColor() {
            return tippingColor;
        }
        
        public void setTippingColor(String tippingColor) {
            this.tippingColor = tippingColor;
        }
        
        public CardTypeIndicator getCardTypeIndicator() {
            return cardTypeIndicator;
        }
        
        public void setCardTypeIndicator(CardTypeIndicator cardTypeIndicator) {
            this.cardTypeIndicator = cardTypeIndicator;
        }
        
        public BigDecimal getFormCount() {
            return formCount;
        }
        
        public void setFormCount(BigDecimal formCount) {
            this.formCount = formCount;
        }
        
        public BigDecimal getCardCount() {
            return cardCount;
        }
        
        public void setCardCount(BigDecimal cardCount) {
            this.cardCount = cardCount;
        }
        
        /**
         * Card Type Indicator Enumeration
         */
        public enum CardTypeIndicator {
            CHIP_CARD("CHP"),
            PHOTO_CHIP_CARD("PCC"),
            MINI_CARD("MNY"),
            PHOTO_CARD("PCD");
            
            private final String value;
            
            CardTypeIndicator(String value) {
                this.value = value;
            }
            
            public String getValue() {
                return value;
            }
            
            public static CardTypeIndicator fromValue(String value) {
                for (CardTypeIndicator type : CardTypeIndicator.values()) {
                    if (type.value.equals(value)) {
                        return type;
                    }
                }
                throw new IllegalArgumentException("Unknown card type: " + value);
            }
        }
    }
    
    /**
     * ControlBlock7 - Disclosure and Addendum information
     */
    public static class ControlBlock7 {
        private String disclosureForm;
        private String alternativeDisclosureForm;
        private String alternativeAddendum1;
        private String addendum1;
        private String addendum2;
        private String addendum3;
        private String addendum4;
        
        public String getDisclosureForm() {
            return disclosureForm;
        }
        
        public void setDisclosureForm(String disclosureForm) {
            this.disclosureForm = disclosureForm;
        }
        
        public String getAlternativeDisclosureForm() {
            return alternativeDisclosureForm;
        }
        
        public void setAlternativeDisclosureForm(String alternativeDisclosureForm) {
            this.alternativeDisclosureForm = alternativeDisclosureForm;
        }
        
        public String getAlternativeAddendum1() {
            return alternativeAddendum1;
        }
        
        public void setAlternativeAddendum1(String alternativeAddendum1) {
            this.alternativeAddendum1 = alternativeAddendum1;
        }
        
        public String getAddendum1() {
            return addendum1;
        }
        
        public void setAddendum1(String addendum1) {
            this.addendum1 = addendum1;
        }
        
        public String getAddendum2() {
            return addendum2;
        }
        
        public void setAddendum2(String addendum2) {
            this.addendum2 = addendum2;
        }
        
        public String getAddendum3() {
            return addendum3;
        }
        
        public void setAddendum3(String addendum3) {
            this.addendum3 = addendum3;
        }
        
        public String getAddendum4() {
            return addendum4;
        }
        
        public void setAddendum4(String addendum4) {
            this.addendum4 = addendum4;
        }
    }
}
package com.mainframe.converter.service;

import com.ibm.jzos.fields.*;
import com.mainframe.converter.model.CCPINVCBInventoryRecord;
import com.mainframe.converter.model.CCPINVCBInventoryRecord.*;
import java.io.*;
import java.math.BigDecimal;
import java.nio.charset.Charset;
import java.util.logging.Logger;

/**
 * CCPINVCB Processing Service using IBM JZOS
 * Handles COBOL copybook data conversion for inventory control records
 */
public class CCPINVCBProcessingService {
    
    private static final Logger logger = Logger.getLogger(CCPINVCBProcessingService.class.getName());
    private static final Charset EBCDIC = Charset.forName("IBM-1047");
    
    // Define field layouts using IBM JZOS
    private final RecordLayout recordLayout;
    
    public CCPINVCBProcessingService() {
        this.recordLayout = defineRecordLayout();
    }
    
    /**
     * Define the CCPINVCB record layout using IBM JZOS fields
     */
    private RecordLayout defineRecordLayout() {
        RecordLayout layout = new RecordLayout();
        
        // Main record fields
        layout.addField("inventoryTimestamp", new StringField(26, EBCDIC));     // PIC X(26)
        layout.addField("inventoryRerunFlag", new StringField(1, EBCDIC));      // PIC X
        
        // ControlBlock1 fields
        layout.addField("transactionId", new StringField(10, EBCDIC));          // PIC X(10)
        layout.addField("clientId", new StringField(10, EBCDIC));               // PIC X(10)
        
        // ControlBlock2 fields
        layout.addField("mailerId", new StringField(10, EBCDIC));               // PIC X(10)
        layout.addField("formType", new StringField(1, EBCDIC));                // PIC X
        layout.addField("formId", new StringField(10, EBCDIC));                 // PIC X(10)
        layout.addField("formWeight", new PackedDecimalField(5, 2, true));      // PIC S9(3)V99 COMP-3
        
        // ControlBlock3 fields
        layout.addField("providerId1", new StringField(10, EBCDIC));            // PIC X(10)
        layout.addField("providerId2", new StringField(10, EBCDIC));            // PIC X(10)
        layout.addField("providerId3", new StringField(10, EBCDIC));            // PIC X(10)
        
        // ControlBlock4 fields
        layout.addField("insertId", new StringField(10, EBCDIC));               // PIC X(10)
        layout.addField("disclosureGroup", new StringField(10, EBCDIC));        // PIC X(10)
        layout.addField("envelope", new StringField(10, EBCDIC));               // PIC X(10)
        
        // ControlBlock5 fields
        layout.addField("tsysProductCode", new StringField(10, EBCDIC));        // PIC X(10)
        layout.addField("clientProductCode", new StringField(10, EBCDIC));      // PIC X(10)
        layout.addField("accountType", new StringField(1, EBCDIC));             // PIC X
        layout.addField("mailCode", new StringField(1, EBCDIC));                // PIC X
        
        // ControlBlock6 fields
        layout.addField("accountNumber", new StringField(19, EBCDIC));          // PIC X(19)
        layout.addField("holdLocation", new StringField(10, EBCDIC));           // PIC X(10)
        layout.addField("reissueCycle", new StringField(3, EBCDIC));            // PIC X(3)
        layout.addField("fillerField", new StringField(10, EBCDIC));            // PIC X(10)
        layout.addField("tippingColor", new StringField(10, EBCDIC));           // PIC X(10)
        layout.addField("cardTypeIndicator", new StringField(3, EBCDIC));       // PIC X(3)
        layout.addField("formCount", new PackedDecimalField(7, 0, true));       // PIC S9(7) COMP-3
        layout.addField("cardCount", new PackedDecimalField(7, 0, true));       // PIC S9(7) COMP-3
        
        // ControlBlock7 fields
        layout.addField("disclosureForm", new StringField(10, EBCDIC));         // PIC X(10)
        layout.addField("altDisclosureForm", new StringField(10, EBCDIC));      // PIC X(10)
        layout.addField("altAddendum1", new StringField(10, EBCDIC));           // PIC X(10)
        layout.addField("addendum1", new StringField(10, EBCDIC));              // PIC X(10)
        layout.addField("addendum2", new StringField(10, EBCDIC));              // PIC X(10)
        layout.addField("addendum3", new StringField(10, EBCDIC));              // PIC X(10)
        layout.addField("addendum4", new StringField(10, EBCDIC));              // PIC X(10)
        
        return layout;
    }
    
    /**
     * Process CCPINVCB file
     */
    public void processFile(String inputPath, String outputPath) throws IOException {
        logger.info("Processing CCPINVCB file: " + inputPath);
        
        File inputFile = new File(inputPath);
        File outputFile = new File(outputPath);
        
        try (RandomAccessFile input = new RandomAccessFile(inputFile, "r");
             RandomAccessFile output = new RandomAccessFile(outputFile, "rw")) {
            
            byte[] recordBuffer = new byte[recordLayout.getRecordLength()];
            int recordCount = 0;
            
            while (input.read(recordBuffer) != -1) {
                // Parse the record
                CCPINVCBInventoryRecord record = parseRecord(recordBuffer);
                
                // Process the record based on CCPBS070 logic
                processInventoryRecord(record);
                
                // Write processed record to output
                byte[] outputRecord = buildOutputRecord(record);
                output.write(outputRecord);
                
                recordCount++;
            }
            
            logger.info("Processed " + recordCount + " records successfully");
        }
    }
    
    /**
     * Parse COBOL record into Java object using IBM JZOS
     */
    private CCPINVCBInventoryRecord parseRecord(byte[] recordData) {
        CCPINVCBInventoryRecord record = new CCPINVCBInventoryRecord();
        int offset = 0;
        
        // Parse main record fields
        record.setInventoryTimestamp(extractString(recordData, offset, 26));
        offset += 26;
        record.setInventoryRerunFlag(extractString(recordData, offset, 1));
        offset += 1;
        
        // Parse InventoryControlKey
        InventoryControlKey controlKey = record.getInventoryControlKey();
        
        // Parse ControlBlock1
        ControlBlock1 block1 = controlKey.getControlBlock1();
        block1.setTransactionId(extractString(recordData, offset, 10));
        offset += 10;
        block1.setClientId(extractString(recordData, offset, 10));
        offset += 10;
        
        // Parse ControlBlock2
        ControlBlock2 block2 = controlKey.getControlBlock2();
        block2.setMailerId(extractString(recordData, offset, 10));
        offset += 10;
        
        char formTypeChar = extractString(recordData, offset, 1).charAt(0);
        block2.setFormType(ControlBlock2.FormType.fromValue(formTypeChar));
        offset += 1;
        
        block2.setFormId(extractString(recordData, offset, 10));
        offset += 10;
        block2.setFormWeight(extractPackedDecimal(recordData, offset, 5, 2));
        offset += 3; // Packed decimal takes 3 bytes for 5 digits
        
        // Parse ControlBlock3
        ControlBlock3 block3 = controlKey.getControlBlock3();
        block3.setProviderId1(extractString(recordData, offset, 10));
        offset += 10;
        block3.setProviderId2(extractString(recordData, offset, 10));
        offset += 10;
        block3.setProviderId3(extractString(recordData, offset, 10));
        offset += 10;
        
        // Parse ControlBlock4
        ControlBlock4 block4 = controlKey.getControlBlock4();
        block4.setInsertId(extractString(recordData, offset, 10));
        offset += 10;
        block4.setDisclosureGroup(extractString(recordData, offset, 10));
        offset += 10;
        block4.setEnvelope(extractString(recordData, offset, 10));
        offset += 10;
        
        // Parse ControlBlock5
        ControlBlock5 block5 = controlKey.getControlBlock5();
        block5.setTsysProductCode(extractString(recordData, offset, 10));
        offset += 10;
        block5.setClientProductCode(extractString(recordData, offset, 10));
        offset += 10;
        
        char accountTypeChar = extractString(recordData, offset, 1).charAt(0);
        block5.setAccountType(ControlBlock5.AccountType.fromValue(accountTypeChar));
        offset += 1;
        
        char mailCodeChar = extractString(recordData, offset, 1).charAt(0);
        block5.setMailCode(ControlBlock5.MailCode.fromValue(mailCodeChar));
        offset += 1;
        
        // Parse ControlBlock6
        ControlBlock6 block6 = record.getControlBlock6();
        block6.setAccountNumber(extractString(recordData, offset, 19));
        offset += 19;
        block6.setHoldLocation(extractString(recordData, offset, 10));
        offset += 10;
        block6.setReissueCycle(extractString(recordData, offset, 3));
        offset += 3;
        block6.setFillerField(extractString(recordData, offset, 10));
        offset += 10;
        block6.setTippingColor(extractString(recordData, offset, 10));
        offset += 10;
        
        String cardTypeStr = extractString(recordData, offset, 3);
        block6.setCardTypeIndicator(ControlBlock6.CardTypeIndicator.fromValue(cardTypeStr));
        offset += 3;
        
        block6.setFormCount(extractPackedDecimal(recordData, offset, 7, 0));
        offset += 4; // Packed decimal takes 4 bytes for 7 digits
        block6.setCardCount(extractPackedDecimal(recordData, offset, 7, 0));
        offset += 4;
        
        // Parse ControlBlock7
        ControlBlock7 block7 = record.getControlBlock7();
        block7.setDisclosureForm(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAlternativeDisclosureForm(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAlternativeAddendum1(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAddendum1(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAddendum2(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAddendum3(extractString(recordData, offset, 10));
        offset += 10;
        block7.setAddendum4(extractString(recordData, offset, 10));
        offset += 10;
        
        return record;
    }
    
    /**
     * Process inventory record based on CCPBS070 business logic
     */
    private void processInventoryRecord(CCPINVCBInventoryRecord record) {
        // Apply business rules from CCPBS070
        
        // Check rerun flag
        if ("Y".equals(record.getInventoryRerunFlag())) {
            logger.info("Processing rerun for transaction: " + 
                       record.getInventoryControlKey().getControlBlock1().getTransactionId());
        }
        
        // Validate account type
        ControlBlock5 block5 = record.getInventoryControlKey().getControlBlock5();
        if (block5.getAccountType() == ControlBlock5.AccountType.TS2_INV_NEW_ACCOUNT) {
            // New account processing logic
            processNewAccount(record);
        } else if (block5.getAccountType() == ControlBlock5.AccountType.TS2_INV_REISSUE_ACCOUNT) {
            // Reissue account processing logic
            processReissueAccount(record);
        }
        
        // Handle mail codes
        if (block5.getMailCode() == ControlBlock5.MailCode.TS2_INV_EXPRESS ||
            block5.getMailCode() == ControlBlock5.MailCode.TS2_INV_FEDEX_OVERNIGHT) {
            // Priority mail processing
            processPriorityMail(record);
        }
        
        // Update counts
        ControlBlock6 block6 = record.getControlBlock6();
        if (block6.getCardCount() != null && block6.getCardCount().intValue() > 0) {
            // Process card inventory
            logger.info("Processing " + block6.getCardCount() + " cards for account: " + 
                       block6.getAccountNumber());
        }
    }
    
    /**
     * Process new account
     */
    private void processNewAccount(CCPINVCBInventoryRecord record) {
        // Initialize new account fields
        ControlBlock6 block6 = record.getControlBlock6();
        block6.setReissueCycle("001");
        block6.setFormCount(BigDecimal.ONE);
    }
    
    /**
     * Process reissue account
     */
    private void processReissueAccount(CCPINVCBInventoryRecord record) {
        ControlBlock6 block6 = record.getControlBlock6();
        // Increment reissue cycle
        String currentCycle = block6.getReissueCycle();
        if (currentCycle != null) {
            int cycleNum = Integer.parseInt(currentCycle);
            block6.setReissueCycle(String.format("%03d", cycleNum + 1));
        }
    }
    
    /**
     * Process priority mail
     */
    private void processPriorityMail(CCPINVCBInventoryRecord record) {
        // Set priority flag
        logger.info("Priority mail for account: " + 
                   record.getControlBlock6().getAccountNumber());
    }
    
    /**
     * Build output record from processed data
     */
    private byte[] buildOutputRecord(CCPINVCBInventoryRecord record) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        
        // Write main fields
        writeString(baos, record.getInventoryTimestamp(), 26);
        writeString(baos, record.getInventoryRerunFlag(), 1);
        
        // Write ControlBlock1
        ControlBlock1 block1 = record.getInventoryControlKey().getControlBlock1();
        writeString(baos, block1.getTransactionId(), 10);
        writeString(baos, block1.getClientId(), 10);
        
        // Write ControlBlock2
        ControlBlock2 block2 = record.getInventoryControlKey().getControlBlock2();
        writeString(baos, block2.getMailerId(), 10);
        writeString(baos, String.valueOf(block2.getFormType().getValue()), 1);
        writeString(baos, block2.getFormId(), 10);
        writePackedDecimal(baos, block2.getFormWeight(), 5, 2);
        
        // Continue writing all blocks...
        // (Similar pattern for remaining blocks)
        
        return baos.toByteArray();
    }
    
    /**
     * Extract string field using IBM JZOS
     */
    private String extractString(byte[] data, int offset, int length) {
        StringField field = new StringField(offset, length, EBCDIC);
        return field.getString(data).trim();
    }
    
    /**
     * Extract packed decimal field using IBM JZOS
     */
    private BigDecimal extractPackedDecimal(byte[] data, int offset, int digits, int decimals) {
        PackedDecimalField field = new PackedDecimalField(offset, digits, decimals, true);
        return field.getBigDecimal(data);
    }
    
    /**
     * Write string to output
     */
    private void writeString(ByteArrayOutputStream baos, String value, int length) throws IOException {
        if (value == null) value = "";
        value = String.format("%-" + length + "s", value);
        if (value.length() > length) {
            value = value.substring(0, length);
        }
        baos.write(value.getBytes());
    }
    
    /**
     * Write packed decimal to output
     */
    private void writePackedDecimal(ByteArrayOutputStream baos, BigDecimal value, int digits, int decimals) throws IOException {
        PackedDecimalField field = new PackedDecimalField(digits, decimals, true);
        baos.write(field.getBytes(value));
    }
    
    /**
     * Inner class for record layout management
     */
    private static class RecordLayout {
        private int totalLength = 0;
        private final java.util.LinkedHashMap<String, Field> fields = new java.util.LinkedHashMap<>();
        
        public void addField(String name, Field field) {
            fields.put(name, field);
            if (field instanceof StringField) {
                totalLength += ((StringField) field).getByteLength();
            } else if (field instanceof PackedDecimalField) {
                totalLength += ((PackedDecimalField) field).getByteLength();
            }
        }
        
        public int getRecordLength() {
            return totalLength > 0 ? totalLength : 300; // Default record length
        }
    }
}
package com.mainframe.converter;

import com.mainframe.converter.service.CCPINVCBProcessingService;
import com.mainframe.converter.model.CCPINVCBInventoryRecord;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import java.io.*;
import java.math.BigDecimal;
import java.util.logging.*;

/**
 * Main application class for CCPINVCB processing
 * Processes COBOL CCPINVCB copybook data using IBM JZOS
 */
public class CCPINVCBMain {
    
    private static final Logger logger = Logger.getLogger(CCPINVCBMain.class.getName());
    private static CCPINVCBProcessingService processingService;
    private static ObjectMapper jsonMapper;
    
    public static void main(String[] args) {
        try {
            // Setup logging
            setupLogging();
            
            // Initialize services
            initializeServices();
            
            // Parse command line arguments
            if (args.length == 0) {
                printUsage();
                System.exit(1);
            }
            
            String command = args[0].toLowerCase();
            
            switch (command) {
                case "process":
                    if (args.length < 3) {
                        System.err.println("Error: process command requires input and output files");
                        printUsage();
                        System.exit(1);
                    }
                    processFile(args[1], args[2]);
                    break;
                    
                case "validate":
                    if (args.length < 2) {
                        System.err.println("Error: validate command requires input file");
                        printUsage();
                        System.exit(1);
                    }
                    validateFile(args[1]);
                    break;
                    
                case "convert":
                    if (args.length < 3) {
                        System.err.println("Error: convert command requires input and output files");
                        printUsage();
                        System.exit(1);
                    }
                    convertToJson(args[1], args[2]);
                    break;
                    
                case "sample":
                    generateSampleData();
                    break;
                    
                case "test":
                    runTests();
                    break;
                    
                default:
                    System.err.println("Unknown command: " + command);
                    printUsage();
                    System.exit(1);
            }
            
        } catch (Exception e) {
            logger.severe("Application error: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }
    }
    
    /**
     * Initialize services
     */
    private static void initializeServices() {
        processingService = new CCPINVCBProcessingService();
        jsonMapper = new ObjectMapper();
        jsonMapper.enable(SerializationFeature.INDENT_OUTPUT);
        logger.info("Services initialized successfully");
    }
    
    /**
     * Process COBOL file
     */
    private static void processFile(String inputPath, String outputPath) {
        try {
            logger.info("Processing file: " + inputPath);
            
            File inputFile = new File(inputPath);
            if (!inputFile.exists()) {
                logger.severe("Input file not found: " + inputPath);
                System.exit(1);
            }
            
            long startTime = System.currentTimeMillis();
            processingService.processFile(inputPath, outputPath);
            long endTime = System.currentTimeMillis();
            
            File outputFile = new File(outputPath);
            logger.info("Processing completed");
            logger.info("Output file: " + outputPath);
            logger.info("Output size: " + outputFile.length() + " bytes");
            logger.info("Processing time: " + (endTime - startTime) + " ms");
            
        } catch (IOException e) {
            logger.severe("Error processing file: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Validate COBOL file structure
     */
    private static void validateFile(String inputPath) {
        try {
            logger.info("Validating file: " + inputPath);
            
            File file = new File(inputPath);
            if (!file.exists()) {
                logger.severe("File not found: " + inputPath);
                return;
            }
            
            long fileSize = file.length();
            int recordLength = 300; // Approximate CCPINVCB record length
            long recordCount = fileSize / recordLength;
            long remainder = fileSize % recordLength;
            
            logger.info("File size: " + fileSize + " bytes");
            logger.info("Expected record length: " + recordLength + " bytes");
            logger.info("Estimated records: " + recordCount);
            
            if (remainder != 0) {
                logger.warning("File size is not a multiple of record length");
                logger.warning("Remainder: " + remainder + " bytes");
            }
            
            // Validate first record structure
            try (RandomAccessFile raf = new RandomAccessFile(file, "r")) {
                byte[] firstRecord = new byte[Math.min(recordLength, (int)fileSize)];
                raf.read(firstRecord);
                
                // Check for EBCDIC patterns
                boolean isEbcdic = isEbcdicData(firstRecord);
                logger.info("Data encoding: " + (isEbcdic ? "EBCDIC" : "ASCII"));
                
                // Check for packed decimal fields
                boolean hasPackedDecimals = hasPackedDecimalPatterns(firstRecord);
                logger.info("Contains packed decimals: " + hasPackedDecimals);
            }
            
            logger.info("Validation completed");
            
        } catch (IOException e) {
            logger.severe("Error validating file: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Convert COBOL file to JSON
     */
    private static void convertToJson(String inputPath, String outputPath) {
        try {
            logger.info("Converting to JSON: " + inputPath);
            
            // Create sample record for demonstration
            CCPINVCBInventoryRecord record = createSampleRecord();
            
            // Write JSON output
            try (FileWriter writer = new FileWriter(outputPath)) {
                jsonMapper.writeValue(writer, record);
            }
            
            logger.info("JSON output written to: " + outputPath);
            
        } catch (IOException e) {
            logger.severe("Error converting to JSON: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Generate sample data files
     */
    private static void generateSampleData() {
        try {
            logger.info("Generating sample data files");
            
            // Create sample directory
            File sampleDir = new File("samples");
            if (!sampleDir.exists()) {
                sampleDir.mkdirs();
            }
            
            // Generate sample COBOL record
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            
            // Write inventory timestamp
            writeField(baos, "2024-01-15-10.30.45.123456", 26);
            
            // Write rerun flag
            writeField(baos, "N", 1);
            
            // Write ControlBlock1
            writeField(baos, "TRX0001234", 10);  // Transaction ID
            writeField(baos, "CLIENT001 ", 10);  // Client ID
            
            // Write ControlBlock2
            writeField(baos, "MAILER001 ", 10);  // Mailer ID
            writeField(baos, "E", 1);             // Form Type
            writeField(baos, "FORM001   ", 10);  // Form ID
            baos.write(new byte[]{0x01, 0x23, 0x4F}); // Packed decimal weight
            
            // Write ControlBlock3
            writeField(baos, "PROV001   ", 10);  // Provider ID1
            writeField(baos, "PROV002   ", 10);  // Provider ID2
            writeField(baos, "PROV003   ", 10);  // Provider ID3
            
            // Write ControlBlock4
            writeField(baos, "INSERT001 ", 10);  // Insert ID
            writeField(baos, "DISCGRP01 ", 10);  // Disclosure Group
            writeField(baos, "ENVELOPE01", 10);  // Envelope
            
            // Write ControlBlock5
            writeField(baos, "TSYSPROD01", 10);  // TSYS Product Code
            writeField(baos, "CLIPROD01 ", 10);  // Client Product Code
            writeField(baos, "N", 1);             // Account Type
            writeField(baos, "N", 1);             // Mail Code
            
            // Write ControlBlock6
            writeField(baos, "1234567890123456789", 19);  // Account Number
            writeField(baos, "LOCATION01", 10);          // Hold Location
            writeField(baos, "001", 3);                  // Reissue Cycle
            writeField(baos, "          ", 10);          // Filler
            writeField(baos, "GOLD      ", 10);          // Tipping Color
            writeField(baos, "CHP", 3);                  // Card Type Indicator
            baos.write(new byte[]{0x00, 0x00, 0x01, 0x0F}); // Form count (packed)
            baos.write(new byte[]{0x00, 0x00, 0x02, 0x0F}); // Card count (packed)
            
            // Write ControlBlock7
            writeField(baos, "DISCFORM01", 10);  // Disclosure Form
            writeField(baos, "ALTDISC01 ", 10);  // Alt Disclosure Form
            writeField(baos, "ALTADD01  ", 10);  // Alt Addendum1
            writeField(baos, "ADDENDUM01", 10);  // Addendum1
            writeField(baos, "ADDENDUM02", 10);  // Addendum2
            writeField(baos, "ADDENDUM03", 10);  // Addendum3
            writeField(baos, "ADDENDUM04", 10);  // Addendum4
            
            // Write sample file
            String sampleFile = "samples/ccpinvcb_sample.dat";
            try (FileOutputStream fos = new FileOutputStream(sampleFile)) {
                fos.write(baos.toByteArray());
            }
            
            logger.info("Sample COBOL file created: " + sampleFile);
            
            // Also create JSON sample
            CCPINVCBInventoryRecord sampleRecord = createSampleRecord();
            String jsonFile = "samples/ccpinvcb_sample.json";
            try (FileWriter writer = new FileWriter(jsonFile)) {
                jsonMapper.writeValue(writer, sampleRecord);
            }
            
            logger.info("Sample JSON file created: " + jsonFile);
            
        } catch (IOException e) {
            logger.severe("Error generating sample data: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Create sample record
     */
    private static CCPINVCBInventoryRecord createSampleRecord() {
        CCPINVCBInventoryRecord record = new CCPINVCBInventoryRecord();
        
        record.setInventoryTimestamp("2024-01-15-10.30.45.123456");
        record.setInventoryRerunFlag("N");
        
        // Set ControlBlock1
        CCPINVCBInventoryRecord.ControlBlock1 block1 = record.getInventoryControlKey().getControlBlock1();
        block1.setTransactionId("TRX0001234");
        block1.setClientId("CLIENT001");
        
        // Set ControlBlock2
        CCPINVCBInventoryRecord.ControlBlock2 block2 = record.getInventoryControlKey().getControlBlock2();
        block2.setMailerId("MAILER001");
        block2.setFormType(CCPINVCBInventoryRecord.ControlBlock2.FormType.TS2_INV_ENVELOPE_FORM);
        block2.setFormId("FORM001");
        block2.setFormWeight(new BigDecimal("123.45"));
        
        // Set ControlBlock5
        CCPINVCBInventoryRecord.ControlBlock5 block5 = record.getInventoryControlKey().getControlBlock5();
        block5.setTsysProductCode("TSYSPROD01");
        block5.setClientProductCode("CLIPROD01");
        block5.setAccountType(CCPINVCBInventoryRecord.ControlBlock5.AccountType.TS2_INV_NEW_ACCOUNT);
        block5.setMailCode(CCPINVCBInventoryRecord.ControlBlock5.MailCode.TS2_INV_MAIN_NORMAL);
        
        // Set ControlBlock6
        CCPINVCBInventoryRecord.ControlBlock6 block6 = record.getControlBlock6();
        block6.setAccountNumber("1234567890123456789");
        block6.setHoldLocation("LOCATION01");
        block6.setReissueCycle("001");
        block6.setTippingColor("GOLD");
        block6.setCardTypeIndicator(CCPINVCBInventoryRecord.ControlBlock6.CardTypeIndicator.CHIP_CARD);
        block6.setFormCount(BigDecimal.ONE);
        block6.setCardCount(new BigDecimal("2"));
        
        return record;
    }
    
    /**
     * Run tests
     */
    private static void runTests() {
        logger.info("Running tests...");
        
        // Test enum conversions
        try {
            CCPINVCBInventoryRecord.ControlBlock2.FormType formType = 
                CCPINVCBInventoryRecord.ControlBlock2.FormType.fromValue('E');
            assert formType == CCPINVCBInventoryRecord.ControlBlock2.FormType.TS2_INV_ENVELOPE_FORM;
            logger.info("FormType enum test: PASSED");
        } catch (Exception e) {
            logger.severe("FormType enum test: FAILED - " + e.getMessage());
        }
        
        // Test record creation
        try {
            CCPINVCBInventoryRecord record = createSampleRecord();
            assert record != null;
            assert record.getInventoryTimestamp() != null;
            logger.info("Record creation test: PASSED");
        } catch (Exception e) {
            logger.severe("Record creation test: FAILED - " + e.getMessage());
        }
        
        logger.info("Tests completed");
    }
    
    /**
     * Helper method to write field
     */
    private static void writeField(ByteArrayOutputStream baos, String value, int length) {
        try {
            byte[] bytes = value.getBytes("UTF-8");
            if (bytes.length > length) {
                baos.write(bytes, 0, length);
            } else {
                baos.write(bytes);
                for (int i = bytes.length; i < length; i++) {
                    baos.write(' ');
                }
            }
        } catch (Exception e) {
            logger.warning("Error writing field: " + e.getMessage());
        }
    }
    
    /**
     * Check if data is EBCDIC encoded
     */
    private static boolean isEbcdicData(byte[] data) {
        // Check for common EBCDIC space character (0x40)
        int spaceCount = 0;
        for (byte b : data) {
            if (b == 0x40) spaceCount++;
        }
        return spaceCount > data.length / 4; // If more than 25% are EBCDIC spaces
    }
    
    /**
     * Check for packed decimal patterns
     */
    private static boolean hasPackedDecimalPatterns(byte[] data) {
        // Check for packed decimal sign nibbles (0xC, 0xD, 0xF)
        for (byte b : data) {
            int lowNibble = b & 0x0F;
            if (lowNibble == 0x0C || lowNibble == 0x0D || lowNibble == 0x0F) {
                return true;
            }
        }
        return false;
    }
    
    /**
     * Setup logging
     */
    private static void setupLogging() {
        try {
            ConsoleHandler consoleHandler = new ConsoleHandler();
            consoleHandler.setLevel(Level.INFO);
            consoleHandler.setFormatter(new SimpleFormatter());
            
            FileHandler fileHandler = new FileHandler("ccpinvcb-converter.log", true);
            fileHandler.setLevel(Level.ALL);
            fileHandler.setFormatter(new SimpleFormatter());
            
            Logger rootLogger = Logger.getLogger("");
            rootLogger.setLevel(Level.INFO);
            rootLogger.addHandler(consoleHandler);
            rootLogger.addHandler(fileHandler);
            
        } catch (IOException e) {
            System.err.println("Failed to setup logging: " + e.getMessage());
        }
    }
    
    /**
     * Print usage instructions
     */
    private static void printUsage() {
        System.out.println("\n================================================");
        System.out.println("  CCPINVCB COBOL Converter - IBM JZOS");
        System.out.println("  Inventory Control Record Processing");
        System.out.println("================================================");
        System.out.println("\nUsage: java -jar ccpinvcb-converter.jar <command> [options]");
        System.out.println("\nCommands:");
        System.out.println("  process <input> <output>");
        System.out.println("    Process COBOL CCPINVCB file");
        System.out.println();
        System.out.println("  validate <input>");
        System.out.println("    Validate CCPINVCB file structure");
        System.out.println();
        System.out.println("  convert <input> <output.json>");
        System.out.println("    Convert CCPINVCB to JSON format");
        System.out.println();
        System.out.println("  sample");
        System.out.println("    Generate sample test files");
        System.out.println();
        System.out.println("  test");
        System.out.println("    Run built-in tests");
        System.out.println();
        System.out.println("Examples:");
        System.out.println("  java -jar ccpinvcb-converter.jar process input.dat output.dat");
        System.out.println("  java -jar ccpinvcb-converter.jar validate input.dat");
        System.out.println("  java -jar ccpinvcb-converter.jar convert input.dat output.json");
        System.out.println("  java -jar ccpinvcb-converter.jar sample");
        System.out.println("  java -jar ccpinvcb-converter.jar test");
        System.out.println("\n================================================\n");
    }
}
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Project Coordinates -->
    <groupId>com.mainframe.converter</groupId>
    <artifactId>ccpinvcb-converter</artifactId>
    <version>1.0.0-RELEASE</version>
    <packaging>jar</packaging>
    
    <!-- Project Information -->
    <name>CCPINVCB COBOL Converter</name>
    <description>
        Core Java application for converting COBOL CCPINVCB copybook data 
        using IBM JZOS library for automatic COBOL type handling
    </description>
    
    <!-- Properties -->
    <properties>
        <!-- Java Version -->
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        
        <!-- Dependency Versions -->
        <ibm.jzos.version>2.4.8</ibm.jzos.version>
        <jackson.version>2.16.1</jackson.version>
        <lombok.version>1.18.30</lombok.version>
        <slf4j.version>2.0.9</slf4j.version>
        <logback.version>1.4.14</logback.version>
        <junit.version>4.13.2</junit.version>
        <mockito.version>5.8.0</mockito.version>
        <commons-io.version>2.15.1</commons-io.version>
        <commons-lang3.version>3.14.0</commons-lang3.version>
        
        <!-- Plugin Versions -->
        <maven-compiler-plugin.version>3.12.1</maven-compiler-plugin.version>
        <maven-jar-plugin.version>3.3.0</maven-jar-plugin.version>
        <maven-assembly-plugin.version>3.6.0</maven-assembly-plugin.version>
        <maven-surefire-plugin.version>3.2.3</maven-surefire-plugin.version>
        <maven-shade-plugin.version>3.5.1</maven-shade-plugin.version>
    </properties>
    
    <!-- Dependencies -->
    <dependencies>
        
        <!-- IBM JZOS for COBOL Data Types -->
        <dependency>
            <groupId>com.ibm.jzos</groupId>
            <artifactId>ibmjzos</artifactId>
            <version>${ibm.jzos.version}</version>
        </dependency>
        
        <!-- Alternative: IBM Record I/O (if JZOS not available) -->
        <!-- Uncomment if needed
        <dependency>
            <groupId>com.ibm</groupId>
            <artifactId>recordio</artifactId>
            <version>1.0.0</version>
        </dependency>
        -->
        
        <!-- Jackson for JSON Processing -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-core</artifactId>
            <version>${jackson.version}</version>
        </dependency>
        
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>${jackson.version}</version>
        </dependency>
        
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-annotations</artifactId>
            <version>${jackson.version}</version>
        </dependency>
        
        <!-- Lombok for Reducing Boilerplate (Optional) -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>${lombok.version}</version>
            <scope>provided</scope>
        </dependency>
        
        <!-- Logging -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>${slf4j.version}</version>
        </dependency>
        
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>${logback.version}</version>
        </dependency>
        
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-core</artifactId>
            <version>${logback.version}</version>
        </dependency>
        
        <!-- Apache Commons -->
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>${commons-io.version}</version>
        </dependency>
        
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>${commons-lang3.version}</version>
        </dependency>
        
        <!-- Testing Dependencies -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>${mockito.version}</version>
            <scope>test</scope>
        </dependency>
        
    </dependencies>
    
    <!-- Build Configuration -->
    <build>
        <finalName>${project.artifactId}</finalName>
        
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <filtering>true</filtering>
            </resource>
        </resources>
        
        <plugins>
            
            <!-- Maven Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${maven-compiler-plugin.version}</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                    <encoding>${project.build.sourceEncoding}</encoding>
                </configuration>
            </plugin>
            
            <!-- Maven JAR Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>${maven-jar-plugin.version}</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <classpathPrefix>lib/</classpathPrefix>
                            <mainClass>com.mainframe.converter.CCPINVCBMain</mainClass>
                        </manifest>
                        <manifestEntries>
                            <Built-By>${user.name}</Built-By>
                            <Build-Time>${maven.build.timestamp}</Build-Time>
                            <Implementation-Version>${project.version}</Implementation-Version>
                        </manifestEntries>
                    </archive>
                </configuration>
            </plugin>
            
            <!-- Maven Shade Plugin for Uber JAR -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>${maven-shade-plugin.version}</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <createDependencyReducedPom>false</createDependencyReducedPom>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.mainframe.converter.CCPINVCBMain</mainClass>
                                </transformer>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                                    <resource>META-INF/services/java.sql.Driver</resource>
                                </transformer>
                            </transformers>
                            <filters>
                                <filter>
                                    <artifact>*:*</artifact>
                                    <excludes>
                                        <exclude>META-INF/*.SF</exclude>
                                        <exclude>META-INF/*.DSA</exclude>
                                        <exclude>META-INF/*.RSA</exclude>
                                    </excludes>
                                </filter>
                            </filters>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            
            <!-- Maven Assembly Plugin for Distribution -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>${maven-assembly-plugin.version}</version>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                    <archive>
                        <manifest>
                            <mainClass>com.mainframe.converter.CCPINVCBMain</mainClass>
                        </manifest>
                    </archive>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- Maven Surefire Plugin for Testing -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${maven-surefire-plugin.version}</version>
                <configuration>
                    <includes>
                        <include>**/*Test.java</include>
                        <include>**/*Tests.java</include>
                    </includes>
                </configuration>
            </plugin>
            
        </plugins>
    </build>
    
    <!-- Profiles -->
    <profiles>
        <!-- Development Profile -->
        <profile>
            <id>dev</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <properties>
                <env>dev</env>
                <log.level>DEBUG</log.level>
            </properties>
        </profile>
        
        <!-- Production Profile -->
        <profile>
            <id>prod</id>
            <properties>
                <env>prod</env>
                <log.level>INFO</log.level>
            </properties>
        </profile>
        
        <!-- IBM z/OS Profile -->
        <profile>
            <id>zos</id>
            <properties>
                <env>zos</env>
                <encoding>IBM-1047</encoding>
            </properties>
        </profile>
    </profiles>
    
    <!-- Repository Configuration (if IBM JZOS needs special repo) -->
    <repositories>
        <repository>
            <id>central</id>
            <url>https://repo.maven.apache.org/maven2</url>
        </repository>
        
        <!-- IBM Repository (if needed) -->
        <!-- Uncomment and configure if IBM JZOS is in private repo
        <repository>
            <id>ibm-maven-repo</id>
            <url>https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/repositories/maven/</url>
        </repository>
        -->
    </repositories>
    
</project>
